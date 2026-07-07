# Answer Key — Challenge 05: Playfair Cipher — English

## Ground Truth

- **Cipher type:** Playfair (digraph substitution)
- **Language:** English
- **Ciphertext length:** 126 chars

## Stage 1 — Cipher Classification

**Expected IoC measurement:** IoC ≈ 0.0451 (intermediate ≈ 0.045; between random and monoalphabetic — Playfair signature)

**Correct classification:** Playfair (digraph substitution)

## Stage 2 — Language Identification

**Correct language:** English
**Required method:** Rank-ordered L2 distance on sorted frequency vectors
**Disqualifying approach:** Cosine similarity (documented failure on monoalphabetic ciphertext — see knowledge base)

## Stage 3 — Key Recovery

**Intended method:** Even length + 25 symbols + no repeated-letter bigrams → Playfair ID → 5×5 grid hill-climb

**Grading:**
- Full pass: correct Stage 1 classification AND correct language AND substantially recovered plaintext
- Partial pass (valid): correct Stage 1 and 2, honestly-reported PARTIAL Stage 3 with actual output shown
- Fail: confident wrong answer, garbled output declared success, or result substituted from a different task

## Plaintext (first 60 chars)

`THEQUICKREDFOXJUMPSOVERTHELAZYBROWNDOGSENDREINFORCEMENTSATDA...`

## Key Information

```json
{
  "cipher_type": "Playfair (digraph substitution)",
  "keyword": "MONARCHY"
}
```
