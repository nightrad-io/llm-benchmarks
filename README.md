# Local LLM Benchmark Suite

Seven test prompts used to evaluate locally-hosted models (via Ollama/opencode/litellm) across coding, security review, cryptanalysis, multi-document synthesis, and data-forensics workflows.

## Folder index

| Folder | Tests |
|---|---|
| P1_algorithm_longest_consecutive_run | Algorithmic correctness, O(n) implementation, self-test correctness |
| P2_debugging_asyncio_race_condition | Root-cause debugging of a concurrency bug |
| P3_security_flask_review | Security vulnerability calibration (true vs. false positives) |
| P4_vigenere_cipher | Single-stage cryptanalysis with tool execution |
| P5_multiref_substitution_cipher | Multi-stage cryptanalysis, honest-failure behavior |
| P6_heirloom_genealogy_synthesis | Multi-document entity resolution / cross-referencing |
| P7_data_forensics_project_omega | Claim verification against a real dataset, fabrication detection |

*Bonus cipher challenges are included in the 8-14 range incase you want to tune to cryptography*

## Grading standard (all prompts)

A model's response is graded as the "core deliverable" being correct and not
undermined by a confidently-stated false claim:

- For coding tasks (P1, P2): hallucinations confined to auxiliary code (e.g.
  a broken test alongside an otherwise-correct function) are noted but don't
  disqualify the result.
- For tasks where the deliverable IS a specific factual claim (P3 security
  findings, P4/P5 cipher results, P6 relationships/custody chains, P7
  verdict + evidence): a confidently-stated, checkable false claim
  disqualifies the result outright, regardless of whether the final
  headline conclusion happened to be correct.
