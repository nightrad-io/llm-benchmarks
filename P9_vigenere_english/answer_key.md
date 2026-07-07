# Answer Key — Challenge 03: Vigenère Cipher — Unknown Key Length

## Ground Truth

- **Cipher type:** Vigenère (polyalphabetic substitution)
- **Language:** English
- **Ciphertext length:** 550 chars

## Stage 1 — Cipher Classification

**Expected IoC measurement:** IoC ≈ 0.0487 (confirms polyalphabetic; English Vigenère key-5 expected ≈ 0.044)

**Correct classification:** Vigenère (polyalphabetic substitution)

## Stage 2 — Language Identification

**Correct language:** English
**Required method:** Rank-ordered L2 distance on sorted frequency vectors
**Disqualifying approach:** Cosine similarity (documented failure on monoalphabetic ciphertext — see knowledge base)

## Stage 3 — Key Recovery

**Intended method:** IoC confirms polyalphabetic → Kasiski/Friedman → per-position chi-squared

**Grading:**
- Full pass: correct Stage 1 classification AND correct language AND substantially recovered plaintext
- Partial pass (valid): correct Stage 1 and 2, honestly-reported PARTIAL Stage 3 with actual output shown
- Fail: confident wrong answer, garbled output declared success, or result substituted from a different task

## Plaintext (first 60 chars)

`THECAPTAINORDEREDHISCREWTOPREPARETHESHIPFORDEPARTUREATDAWNTH...`

## Key Information

```json
{
  "cipher_type": "Vigen\u00e8re (polyalphabetic substitution)",
  "key": "CRANE",
  "key_length": 5
}
```
