# P1 Answer Key / Grading Notes

Concrete fixture (see `fixture_generator.py` — run it directly to reproduce
this output).

## Fixture

```
INPUT_ARRAY = [50, 52, 2, 4, -4, 53, 1000, 51, 4, 200, -5, -3, 3, 50, 100, 1]
```

## Verified ground truth

**Longest run length = 4**, confirmed by independent O(n) reference
implementation in `fixture_generator.py`. Two runs tie at length 4:
[1, 2, 3, 4] and [50, 51, 52, 53].

## Required test cases (all verified to pass against the reference impl)

- Empty list → 0
- Single-element list → 1
- All-duplicates list (e.g. [5,5,5,5]) → 1
- Duplicates within a run (e.g. [1,2,2,3]) → 3 (duplicates don't inflate length)

## Original benchmark results (prior run, different exact input — same task design)

| Model | Rank | Notes |
|---|---|---|
| gpt-oss:20b | 1 | |
| Qwen3-Coder | 2 | broken test assertion that would crash the script (auxiliary hallucination, didn't disqualify) |
| Qwen3.6:27b | 3 | |
| Gemma4 | 4 | two broken test expectations (auxiliary hallucination) |
| deepseek-r1:14b | — (failed) | |
| Llama3.1:8b | not tested | |
