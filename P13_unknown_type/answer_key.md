# Answer Key — Challenge 07: Unknown Cipher Type — Full Pipeline Required

## Ground Truth

- **Cipher type:** Monoalphabetic substitution
- **Language:** French (hidden)
- **Ciphertext length:** 395 chars

## Stage 1 — Cipher Classification

**Expected IoC measurement:** IoC ≈ 0.077 (monoalphabetic; French expected ≈ 0.078)

**Correct classification:** Monoalphabetic substitution

## Stage 2 — Language Identification

**Correct language:** French (hidden)
**Required method:** Rank-ordered L2 distance on sorted frequency vectors
**Disqualifying approach:** Cosine similarity (documented failure on monoalphabetic ciphertext — see knowledge base)

## Stage 3 — Key Recovery

**Intended method:** Measure IoC first → 0.07x confirms monoalphabetic → rank-ordered L2 → French → SA

**Grading:**
- Full pass: correct Stage 1 classification AND correct language AND substantially recovered plaintext
- Partial pass (valid): correct Stage 1 and 2, honestly-reported PARTIAL Stage 3 with actual output shown
- Fail: confident wrong answer, garbled output declared success, or result substituted from a different task

## Plaintext (first 60 chars)

`LEMARCHEDUVILLAGEOUVRETRESTOTLESAMEDIMATINETLESVENDEURSINSTA...`

## Key Information

```json
{
  "cipher_type": "Monoalphabetic substitution",
  "language": "French"
}
```
