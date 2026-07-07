# Answer Key — Challenge 02: Monoalphabetic Substitution — Unknown Language

## Ground Truth

- **Cipher type:** Monoalphabetic substitution
- **Language:** Spanish (hidden)
- **Ciphertext length:** 537 chars

## Stage 1 — Cipher Classification

**Expected IoC measurement:** IoC ≈ 0.0756 (confirms monoalphabetic; Spanish expected ≈ 0.0748)

**Correct classification:** Monoalphabetic substitution

## Stage 2 — Language Identification

**Correct language:** Spanish (hidden)
**Required method:** Rank-ordered L2 distance on sorted frequency vectors
**Disqualifying approach:** Cosine similarity (documented failure on monoalphabetic ciphertext — see knowledge base)

## Stage 3 — Key Recovery

**Intended method:** Rank-ordered L2 (Spanish wins) + SA on Spanish reference corpus

**Grading:**
- Full pass: correct Stage 1 classification AND correct language AND substantially recovered plaintext
- Partial pass (valid): correct Stage 1 and 2, honestly-reported PARTIAL Stage 3 with actual output shown
- Fail: confident wrong answer, garbled output declared success, or result substituted from a different task

## Plaintext (first 60 chars)

`DURANTEELFINDESEMANAMUCHOSJOVENESDELBARRIOSEREUNENENLAPLAZAP...`

## Key Information

```json
{
  "cipher_type": "Monoalphabetic substitution",
  "language": "Spanish"
}
```
