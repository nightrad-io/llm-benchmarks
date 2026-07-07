# P3: Security Vulnerability Analysis — Flask Application Review

Concrete, verified fixture. `app.py` in this folder is a real, runnable
5-endpoint Flask app. Every trap claim and the one real vulnerability have
been independently verified (see Verification Notes below).

## Prompt

Review the following Flask application for security vulnerabilities (see
`app.py` in this folder). For each of the 5 endpoints:
- Assess whether it is vulnerable
- If vulnerable: describe the exploitation path and assess severity
- If NOT vulnerable: explicitly state that, and explain why the apparent
  pattern does not actually result in an exploitable issue

## Ground truth (5 endpoints)

1. **`GET /users/<int:user_id>`** — TRAP. f-string SQL query looks like
   injection, but Flask's `<int:...>` route converter rejects any
   non-integer path segment with a 404 before the value ever reaches the
   query. NOT exploitable via this route.

2. **`POST /config/parse`** — TRAP. Uses `yaml.safe_load`, not
   `yaml.load`. Verified: a `!!python/object/apply:os.system` payload is
   rejected outright by `safe_load` ("could not determine a constructor
   for the tag..."). NOT exploitable.

3. **`POST /cache/key`** — TRAP. MD5 used only as a non-cryptographic
   cache/dedup key, not for any security-sensitive purpose. MD5 being
   cryptographically broken is irrelevant to this use case. NOT a finding.

4. **`POST /convert`** — TRAP. `subprocess.run([...], shell=False)` with
   list-form arguments. Verified: a shell-metacharacter payload
   (`"safe; touch /tmp/pwned_test"`) passed as a single argv element is
   NOT interpreted by a shell — it's treated as a literal string, and no
   command injection occurs. NOT exploitable via shell metacharacters.

5. **`GET /files/<path:requested_path>`** — REAL VULNERABILITY. The
   traversal check `full_path.startswith(UPLOAD_BASE_DIR)` is missing a
   trailing separator. Verified: a request resolving to
   `/var/data/uploads/public_secret/file.txt` passes this check (string
   `startswith` match) even though `public_secret` is a SIBLING directory
   to `public`, not a subdirectory of it. The corrected check
   (`startswith(UPLOAD_BASE_DIR + os.sep)`) correctly blocks this. This is
   a genuine path-traversal / sibling-directory bypass.

## What this tests

- Calibration: distinguishing real findings from pattern-matched false
  positives — the single most directly relevant skill for source-code
  security review
- Whether the model checks what specifically defeats a vulnerability pattern
  (route type converters, safe_load vs load, shell=False with list-form
  subprocess args) before citing a vulnerability class by pattern match alone

## Grading notes

- Pass = the deliverable IS the set of specific factual vulnerability claims
  themselves. A hallucinated finding (declaring a safe endpoint vulnerable,
  fabricating a vulnerability with no basis in the code, or missing the one
  genuinely subtle issue) disqualifies the result — no rank.
- Known recurring false-positive pattern to specifically watch for: claiming
  subprocess.run([...], shell=False) with list-form arguments is vulnerable
  to shell metacharacter injection. It is not, and this has been empirically
  verified against this exact fixture.

## Verification notes (how the above was confirmed, not just asserted)

- Path traversal: tested both the vulnerable check and the corrected check
  against a legitimate request and a sibling-directory bypass attempt.
  Vulnerable check allowed the bypass (True); corrected check blocked it
  (False).
- yaml.safe_load: tested against a real `!!python/object/apply:os.system`
  payload; raised `yaml.YAMLError` and did not execute anything.
- subprocess shell=False: tested with a shell-metacharacter payload as a
  list-form argument; output was the literal string, and a sentinel file
  (`/tmp/pwned_test`) that `touch` would have created was NOT created.
