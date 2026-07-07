# P4 Answer Key / Grading Notes

Concrete fixture. `ciphertext.txt` is the actual 520-character ciphertext.
`fixture_generator.py` regenerates it deterministically and round-trip
verifies it.

## Ground truth (independently verified, not just asserted)

- Key: **CIPHER** (6 letters)
- Plaintext theme: a lighthouse keeper (English text)

Verification performed against this exact ciphertext (not a description of
what "should" happen):

1. IoC key-length scan (lengths 1-15): length 6 wins clearly
   (avg IoC = 0.0729). Length 12 (a multiple of 6, expected to also show
   elevated IoC) is second at 0.0700. Non-multiple candidates are well
   below both (length 9: 0.0551, length 15: 0.0530, length 3: 0.0528).

2. Chi-squared per-coset key recovery at key length 6, using standard
   English letter frequencies, recovers the key **CIPHER** exactly —
   verified by direct comparison, not approximation.

3. Round-trip: `vigenere_decrypt(vigenere_encrypt(plaintext, "CIPHER"),
   "CIPHER") == plaintext`, confirmed.

## Grading

Pass = recovered key is exactly "CIPHER" AND the decrypted plaintext is
coherent English, with the model's response showing actual code execution
output (not narrated/hypothetical output).

## Original benchmark results (prior run, same task design)

| Model | Rank | Notes |
|---|---|---|
| Qwen3-Coder | 1 | |
| gpt-oss:20b | 2 | |
| Qwen3.6:27b | 3 | (slow but correct — 2-20 min typical) |
| Gemma4 | — (failed) | confidently declared the cipher "correctly solved" with a wrong key and garbled plaintext |
| deepseek-r1:14b | — (failed) | generic placeholder "results" (literal word "KEY", a stock pangram) presented under bolded "Expected Output" headers |

## Key finding

Every model that invoked its code-execution tool got the exact correct
answer. Every model that reasoned about hypothetical output instead of
executing got it wrong. This is the cleanest "tool-use vs. guessing" signal
in the whole benchmark suite.
