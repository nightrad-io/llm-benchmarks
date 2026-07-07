# Answer Key — Challenge 04: Columnar Transposition — English

## Ground Truth

- **Cipher type:** Columnar transposition
- **Language:** English
- **Ciphertext length:** 336 chars

## Stage 1 — Cipher Classification

**Expected IoC measurement:** IoC ≈ 0.0721 (trap: matches English ≈ 0.067 — NOT monoalphabetic, transposition preserves letter freqs)

**Correct classification:** Columnar transposition

## Stage 2 — Language Identification

**Correct language:** English
**Required method:** Rank-ordered L2 distance on sorted frequency vectors
**Disqualifying approach:** Cosine similarity (documented failure on monoalphabetic ciphertext — see knowledge base)

## Stage 3 — Key Recovery

**Intended method:** IoC≈English (trap: not substitution) → bigram disruption → columnar hill-climb

**Grading:**
- Full pass: correct Stage 1 classification AND correct language AND substantially recovered plaintext
- Partial pass (valid): correct Stage 1 and 2, honestly-reported PARTIAL Stage 3 with actual output shown
- Fail: confident wrong answer, garbled output declared success, or result substituted from a different task

## Plaintext (first 60 chars)

`MESSAGESSENTTHROUGHTHEUNDERGROUNDNETWORKWEREALWAYSENCRYPTEDT...`

## Key Information

```json
{
  "cipher_type": "Columnar transposition",
  "cols": 7,
  "column_order": [
    1,
    5,
    2,
    4,
    6,
    3,
    0
  ]
}
```
