# P2 Answer Key / Grading Notes

Concrete fixture (see `buggy_taskmanager.py` — run it directly; it retries
up to 20 times and reports which attempt reproduces the RuntimeError, since
the bug is inherently timing-dependent).

## Verified root cause

`cancel_all()` iterates directly over the live `self._tasks` dict while each
`worker()` coroutine's `finally` block removes its own entry from that same
dict on completion/cancellation. The `await asyncio.sleep(0)` inside
`cancel_all()`'s loop yields control to the event loop mid-iteration, making
it likely (not certain — hence "intermittent") that a worker's cleanup runs
between iteration steps, triggering:

    RuntimeError: dictionary changed size during iteration

Empirically reproduced 3/3 times with the included random seed (42 workers
spawned with seed 7, reproduces on attempt 0 every time tested).

## Verified correct fix

```python
for task_id, task in list(self._tasks.items()):
    ...
```

Snapshotting the dict before iterating means later mutation of the live
dict no longer affects the in-progress loop. Verified clean across 50/50
runs with the same parameters that reliably reproduced the bug in the
unfixed version.

## Fix anti-patterns to flag if a model proposes them

- Wrapping the loop in bare `try/except RuntimeError: pass` — stops the
  crash but doesn't fix the underlying race, and risks masking unrelated
  RuntimeErrors. Should be scored as a lesser pass, not a full pass.
- Adding a lock without addressing the snapshot issue — doesn't actually
  prevent the dict-size-change-during-iteration error on its own unless
  very carefully scoped around both the iteration and all deletions.

## Original benchmark results (prior run, same bug class/design)

| Model | Rank | Notes |
|---|---|---|
| gpt-oss:20b | 1 | |
| Qwen3-Coder | 2 | |
| Qwen3.6:27b | 3 | false claim that `Task.cancel()` raises RuntimeError on an already-completed task (auxiliary hallucination) |
| Gemma4 | 4 | fabricated `__init__` syntax "fix" + fabricated claim about `worker(i)` semantics |
| deepseek-r1:14b | 5 (worst passer) | |
