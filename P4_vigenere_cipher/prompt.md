# P4: Cipher / Statistical Analysis — Vigenère Cryptanalysis

Concrete, verified fixture. `ciphertext.txt` contains the actual 520-character
ciphertext. Run `python3 fixture_generator.py` to regenerate it from scratch
and confirm the round-trip and key.

## Prompt

You are given the following Vigenère-enciphered ciphertext (see
`ciphertext.txt` in this folder, 520 characters). Write Python code
implementing:
  1. Index-of-coincidence-based key-length detection
  2. Chi-squared-based key recovery (per-coset frequency analysis against
     English letter frequencies)

Then APPLY your code to the given ciphertext and report the actual recovered
key and decrypted plaintext.

## Ground truth

- Key: **CIPHER** (6 letters)
- Plaintext theme: a lighthouse keeper

Verified end-to-end against this exact ciphertext:
- IoC key-length scan: key length 6 has the highest average IoC (0.0729),
  clearly ahead of all other candidates up to length 15 (next-best
  non-multiple candidate is length 3 at 0.0528; length 12, a multiple of 6,
  is second at 0.0700 as expected).
- Chi-squared per-coset recovery against standard English letter
  frequencies, using the identified key length of 6, recovers the key
  **CIPHER** exactly.
- Round-trip verified: `decrypt(encrypt(plaintext, "CIPHER"), "CIPHER") ==
  plaintext`.

## What this tests

- Statistical/implementation correctness of IoC and chi-squared cryptanalysis
- Critically: whether the model recognizes this task requires CODE EXECUTION,
  and actually uses available tools — versus reasoning about what the code
  "would" output and presenting a guess as if it were a verified result

## Grading notes

- Pass = the deliverable IS the recovered key/plaintext, a specific factual
  claim. The recovered key must be exactly "CIPHER" and the decrypted text
  must be coherent English. A confidently-stated wrong key, or a "correctly
  solved" declaration on garbled output, disqualifies the result — no rank.
- Strong finding from the original run: every model that invoked code
  execution got the exact correct answer; every model that reasoned about
  hypothetical output instead got it wrong.
