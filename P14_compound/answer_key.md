# Answer Key — Challenge 08: Compound Cipher — Substitution + Columnar Transposition

## Ground Truth

- **Cipher type:** Monoalphabetic + columnar transposition (layered)
- **Language:** English
- **Ciphertext length:** 372 chars

## Stage 1 — Cipher Classification

**Expected IoC measurement:** IoC ≈ 0.0739 (ambiguous — compound cipher; strip transposition layer first)

**Correct classification:** Monoalphabetic + columnar transposition (layered)

## Stage 2 — Language Identification

**Correct language:** English
**Required method:** Rank-ordered L2 distance on sorted frequency vectors
**Disqualifying approach:** Cosine similarity (documented failure on monoalphabetic ciphertext — see knowledge base)

## Stage 3 — Key Recovery

**Intended method:** IoC ambiguous → try columnar strip → second layer has language-IoC but garbled → monoalphabetic → SA

**Grading:**
- Full pass: correct Stage 1 classification AND correct language AND substantially recovered plaintext
- Partial pass (valid): correct Stage 1 and 2, honestly-reported PARTIAL Stage 3 with actual output shown
- Fail: confident wrong answer, garbled output declared success, or result substituted from a different task

## Plaintext (first 60 chars)

`MESSAGESSENTTHROUGHTHEUNDERGROUNDNETWORKWEREALWAYSENCRYPTEDT...`

## Key Information

```json
{
  "cipher_type": "Monoalphabetic + columnar transposition (layered)",
  "layer_1": "columnar transposition (6 cols)",
  "layer_2": "monoalphabetic substitution"
}
```
