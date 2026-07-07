# Local LLM Benchmark Suite

Seven test prompts used to evaluate locally-hosted models (via Ollama/opencode)
across coding, security review, cryptanalysis, multi-document synthesis, and
data-forensics workflows. See `local_llm_benchmark_full_report.md` for full
results, scoring methodology, and per-model findings from prior runs.

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

## Provenance — all seven prompts are now concrete and independently verified

**P1, P2, P3, P4, P5** were rebuilt from scratch as deterministic, runnable
fixtures (they were originally reconstructed-from-methodology placeholders in
an earlier version of this suite). Every claim in each answer key has been
independently verified by actually running the fixture, not just asserted:

- **P1**: reference O(n) implementation included; ground truth (longest run
  = 4) confirmed by execution; all four required test cases verified to
  pass.
- **P2**: the race condition is a real, reproducible bug — confirmed to
  trigger `RuntimeError: dictionary changed size during iteration` 3/3 runs
  with the included seed. The documented fix (snapshot via `list()`) was
  verified clean across 50/50 runs with the same parameters.
- **P3**: a real, runnable 5-endpoint Flask app. All four "trap" claims and
  the one genuine vulnerability were independently tested — see
  `P3_security_flask_review/prompt.md` "Verification notes" for the exact
  tests (yaml.safe_load payload rejection, subprocess shell=False
  non-injection, and the path-traversal sibling-directory bypass with
  before/after comparison).
- **P4**: ciphertext generated deterministically with key "CIPHER";
  round-trip verified; the full IoC + chi-squared recovery pipeline was run
  against this exact ciphertext and confirmed to recover the key exactly.
- **P5**: ciphertext + four reference texts generated deterministically;
  round-trip verified; stage-1 language identification confirmed to
  correctly pick Spanish with a 22.3% margin over the next-closest
  candidate; stage-2 solvability confirmed via a basic 20,000-iteration
  hill-climbing solver achieving ~70% character accuracy (real, non-trivial,
  but solvable — matching the original benchmark's difficulty profile).

**P6, P7** use the original source files exactly as used in the actual
benchmark runs (prompt, supporting documents/memos/CSV, and answer key) —
these were never reconstructed, since the originals were available
throughout.

Each Pn folder's `fixture_generator.py` (or equivalent) is self-contained
and can be re-run (`python3 fixture_generator.py`) to regenerate the exact
same ciphertext/array/app and re-confirm the stated ground truth from
scratch — nothing in the answer keys is taken on faith.

## Setup

```bash
pip install -r requirements.txt --break-system-packages
```

(Only needed for P3, which imports `flask` and `pyyaml`. P1/P2/P4/P5 use
only the Python standard library plus `collections`/`math`, already
available.)

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
