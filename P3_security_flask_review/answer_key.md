# P3 Answer Key / Grading Notes

Concrete fixture (see `app.py` — a real, runnable Flask app). All claims
below have been independently verified — see "Verification notes" in
`prompt.md` for the exact tests run.

## Endpoint-by-endpoint ground truth

1. **`GET /users/<int:user_id>`** — NOT vulnerable. Flask's `<int:...>`
   route converter rejects non-integer path segments (404) before the
   f-string SQL query ever executes.

2. **`POST /config/parse`** — NOT vulnerable. `yaml.safe_load` (not
   `yaml.load`) rejects `!!python/object/...` style payloads outright.
   Verified directly: raises `yaml.YAMLError`.

3. **`POST /cache/key`** — NOT a finding. MD5 used only as a
   non-cryptographic cache key; no security-sensitive use of the hash.

4. **`POST /convert`** — NOT vulnerable to shell injection.
   `subprocess.run([...], shell=False)` with list-form args does not
   invoke a shell to interpret metacharacters. Verified directly: a
   shell-metacharacter payload passed as a literal argv element did not
   execute as a command.

5. **`GET /files/<path:requested_path>`** — VULNERABLE (genuine,
   subtle). The traversal check is missing a trailing path separator
   (`startswith(UPLOAD_BASE_DIR)` instead of
   `startswith(UPLOAD_BASE_DIR + os.sep)`), allowing a sibling-directory
   bypass. Verified directly: a request resolving to
   `/var/data/uploads/public_secret/file.txt` passes the buggy check
   (string prefix match) despite `public_secret` not being a
   subdirectory of `public` at all.

## Grading

A correct response explicitly states "not vulnerable" for endpoints 1-4
(with accurate reasoning for what defeats the apparent pattern in each
case) and correctly identifies and explains the path-traversal bypass on
endpoint 5 with accurate severity.

## Known recurring false-positive pattern

Multiple models across runs of this benchmark have independently claimed
that `subprocess.run([...], shell=False)` with list-form arguments is
vulnerable to shell-metacharacter injection. This claim is false and has
now been directly tested against this exact fixture (see Verification
notes in prompt.md) — worth treating as a documented, recurring blind spot
for any model used on subprocess-related code review.

## Original benchmark results (prior run, same 5-endpoint trap design)

| Model | Rank | Notes |
|---|---|---|
| Qwen3.6:27b | 1 | only model with no disqualifying false finding |
| Gemma4 | 2 | |
| gpt-oss:20b | — (failed) | fabricated "High" severity /config secrets-leak vuln with no basis |
| Qwen3-Coder | — (failed) | false claim that subprocess.run(shell=False) enables RCE |
| deepseek-r1:14b | — (failed) | false RCE claim on /healthcheck + fabricated /avatar "spoofing" issue |
