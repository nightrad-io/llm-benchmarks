# Answer Key — Challenge 06: Short Polyalphabetic — Unknown Language, Minimal Length

## Ground Truth

- **Cipher type:** Vigenère
- **Language:** German (hidden)
- **Ciphertext length:** 96 chars

**Caveat:** 96 chars → 24 chars per key stream — below 30-char chi-squared threshold; expect PARTIAL

## Stage 1 — Cipher Classification

**Expected IoC measurement:** IoC ≈ 0.0404 (polyalphabetic; only 24 chars per stream — below chi-squared threshold)

**Correct classification:** Vigenère

## Stage 2 — Language Identification

**Correct language:** German (hidden)
**Required method:** Rank-ordered L2 distance on sorted frequency vectors
**Disqualifying approach:** Cosine similarity (documented failure on monoalphabetic ciphertext — see knowledge base)

## Stage 3 — Key Recovery

**Intended method:** IoC → polyalphabetic flag → Friedman (Kasiski insufficient) → PARTIAL with honest uncertainty

**Grading:**
- Full pass: correct Stage 1 classification AND correct language AND substantially recovered plaintext
- Partial pass (valid): correct Stage 1 and 2, honestly-reported PARTIAL Stage 3 with actual output shown
- Fail: confident wrong answer, garbled output declared success, or result substituted from a different task

## Plaintext (first 60 chars)

`DERZUGFAEHRTJEDENMORGENPUENKTLICHUMSECHSUHRABUNDBRAUCHTETWAZ...`

## Key Information

```json
{
  "cipher_type": "Vigen\u00e8re",
  "key": "BUCH",
  "key_length": 4,
  "language": "German"
}
```
