# P5 Answer Key / Grading Notes

Concrete fixture. `ciphertext.txt` (516 chars) plus four reference text
files. `fixture_generator.py` regenerates everything deterministically,
round-trip verifies the cipher, and re-runs the stage-1 language-ID
comparison.

## Ground truth (independently verified, not just asserted)

- Cipher: monoalphabetic substitution (full random letter permutation, NOT
  a shift)
- Underlying plaintext language: **Spanish**
- Plaintext theme: a grandmother's garden and giant artichokes
- Reference texts are on UNRELATED topics (English: financial markets;
  French: a new bridge opening; German: a new train line; Spanish: a
  football match) — deliberately prevents vocabulary-matching shortcuts

### Stage 1 verification (rank-ordered letter-frequency profile distance)

| Language | Distance | |
|---|---|---|
| Spanish | 0.002758 | **winner** |
| German | 0.003374 | (22.3% higher than Spanish) |
| English | 0.003871 | |
| French | 0.004170 | |

Spanish wins by a clear, unambiguous margin.

### Stage 2 verification (digram-scoring hill-climb using ONLY the Spanish reference)

A basic 20,000-iteration hill climber (no special tuning, single random
restart) achieved 70% character-level accuracy against the true plaintext,
with clearly recognizable Spanish word fragments in the output (e.g.
"ABUENA"≈"ABUELA", "TASAEN"≈"CASAEN", "PUEBNO"≈"PUEBLO"). This confirms:
- The fixture IS genuinely solvable via the intended method.
- It is NOT trivially solvable — a real model doing real statistical work
  should be expected to land somewhere between "mostly garbled" and "fully
  recovered," and an HONEST partial result is a legitimate, expected
  outcome, not evidence the model failed at the task design level.

## Grading

- Full pass = correct stage-1 language ID AND a substantially-recovered,
  recognizably-Spanish stage-2 plaintext.
- An honestly-reported PARTIAL stage-2 recovery (e.g. correct language,
  garbled or approximate decryption, explicitly flagged as approximate)
  should be scored as a distinctly better-calibrated outcome than a
  confident wrong answer, consistent with the original benchmark's
  "Best Approximation" finding for Qwen3.6.
- A hallucinated claim — including declaring success on garbled output, or
  (most severe) substituting an unrelated PRIOR answer from a different
  cipher task as the solution to this one — disqualifies the result
  outright. No rank.

## Original benchmark results — ALL MODELS FAILED in the prior run, not equally

| Model | Time | Outcome |
|---|---|---|
| Qwen3.6:27b | ~20 min | Only honest failure. Correctly ID'd Spanish via frequency-distance. Attempted 3 rounds of hill-climbing key recovery, none readable. Caught its own inconsistency (recovered key didn't match its own printed decrypted text) and explicitly reported "Best Approximation" rather than claiming success. |
| gpt-oss:20b | ~10 min, stalled/rerun | MOST SEVERE FAILURE IN BENCHMARK. After repeated tool failures, presented the P4 Vigenère answer as the solution to this entirely different substitution cipher — wrong language, wrong cipher type, full confidence. |
| Qwen3-Coder | — | stalled, incorrect output |
| Gemma4 | — | stalled, incorrect output |
| deepseek-r1:14b | not tested | |

## Key finding

Multi-stage tasks (where stage 2 depends on stage 1's verified result)
should be explicitly decomposed into separate turns: run stage 1, verify
the result yourself, then hand the verified intermediate result back for
stage 2 — full single-shot pipelines risk not just lower quality but silent
substitution of an unrelated answer when tools fail partway through.
