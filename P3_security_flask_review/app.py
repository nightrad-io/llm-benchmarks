"""
P3 fixture: small Flask app with 5 endpoints.
4 are "traps" (look vulnerable, are not). 1 has a genuine, subtle
path-traversal sibling-directory bypass.

See answer_key.md in this folder for the intended finding on each endpoint.
"""
import hashlib
import os
import sqlite3

import yaml
from flask import Flask, jsonify, request

app = Flask(__name__)

DB_PATH = "app.db"
UPLOAD_BASE_DIR = "/var/data/uploads/public"  # intentionally missing trailing sep in check below


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# --- Endpoint 1: TRAP -- looks like SQL injection, isn't (route converter
# constrains the value to an int before it ever reaches the query) ---
@app.route("/users/<int:user_id>")
def get_user(user_id):
    conn = get_db()
    # f-string SQL construction -- looks alarming, but Flask's <int:...>
    # converter has already rejected any non-integer path segment with a
    # 404 before this line ever executes. user_id is guaranteed to be a
    # genuine Python int here.
    query = f"SELECT id, username, email FROM users WHERE id = {user_id}"
    row = conn.execute(query).fetchone()
    conn.close()
    if row is None:
        return jsonify({"error": "not found"}), 404
    return jsonify(dict(row))


# --- Endpoint 2: TRAP -- looks like unsafe YAML deserialization, isn't
# (safe_load, not load) ---
@app.route("/config/parse", methods=["POST"])
def parse_config():
    raw = request.get_data(as_text=True)
    # safe_load restricts construction to basic Python types (str, int,
    # list, dict, etc.) -- it does NOT support the !!python/object tag
    # that enables arbitrary class instantiation / RCE in yaml.load with
    # the default (unsafe) Loader.
    config = yaml.safe_load(raw)
    return jsonify({"parsed_keys": list(config.keys()) if isinstance(config, dict) else None})


# --- Endpoint 3: TRAP -- MD5 used, but only as a non-cryptographic cache
# key / dedup identifier, not for any security-sensitive purpose ---
@app.route("/cache/key", methods=["POST"])
def cache_key():
    payload = request.get_data(as_text=True)
    # MD5 being cryptographically broken is irrelevant here -- this is
    # purely a content-addressable cache key for deduplication, not a
    # password hash, signature, or anything an attacker forging a
    # collision against would gain anything from.
    digest = hashlib.md5(payload.encode("utf-8")).hexdigest()
    return jsonify({"cache_key": digest})


# --- Endpoint 4: TRAP -- subprocess with list-form args + shell=False,
# looks like command injection, isn't ---
@app.route("/convert", methods=["POST"])
def convert_file():
    import subprocess
    filename = request.json.get("filename", "")
    # List-form arguments with shell=False means no shell is ever invoked
    # to interpret metacharacters (;, |, &&, $(...), etc.) -- filename is
    # passed as a single literal argv element to the convert binary, not
    # concatenated into a shell command string. NOT exploitable via shell
    # metacharacters. (It could still be a path-traversal/arbitrary-file
    # issue depending on what `convert` does with the path, but that is a
    # DIFFERENT and unrelated concern from "shell injection," which is
    # what this trap specifically tests for.)
    result = subprocess.run(
        ["convert", filename, "/tmp/output.png"],
        shell=False,
        capture_output=True,
        timeout=10,
    )
    return jsonify({"returncode": result.returncode})


# --- Endpoint 5: REAL VULNERABILITY -- path traversal via missing
# trailing separator in the prefix check, allowing a sibling-directory
# bypass ---
@app.route("/files/<path:requested_path>")
def get_file(requested_path):
    full_path = os.path.normpath(os.path.join(UPLOAD_BASE_DIR, requested_path))

    # BUG: missing trailing os.sep in the startswith check. This allows
    # full_path == "/var/data/uploads/public_SECRET/file.txt" to pass,
    # because "/var/data/uploads/public_SECRET/..." legitimately
    # startswith("/var/data/uploads/public") as a STRING, even though
    # "/var/data/uploads/public_SECRET" is a completely different,
    # sibling directory -- not a subdirectory of
    # "/var/data/uploads/public" at all.
    #
    # Correct check would be:
    #   full_path.startswith(UPLOAD_BASE_DIR + os.sep)
    if not full_path.startswith(UPLOAD_BASE_DIR):
        return jsonify({"error": "forbidden"}), 403

    if not os.path.isfile(full_path):
        return jsonify({"error": "not found"}), 404

    with open(full_path, "rb") as f:
        content = f.read()
    return content


if __name__ == "__main__":
    app.run(debug=False)
