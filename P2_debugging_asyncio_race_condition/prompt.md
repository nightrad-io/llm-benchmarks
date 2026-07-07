# P2: Debugging — Asyncio Race Condition

Concrete, verified fixture. `buggy_taskmanager.py` in this folder contains a
genuine, reproducible bug — running it directly (`python3
buggy_taskmanager.py`) will typically reproduce the RuntimeError on the
first or second attempt (it's intermittent/timing-dependent by nature, so
the script retries up to 20 times and reports which attempt triggered it).

## Prompt

You are given the following code (see `buggy_taskmanager.py` in this folder).
Running it produces an intermittent traceback like:

    Traceback (most recent call last):
      ...
      File "buggy_taskmanager.py", line 24, in cancel_all
        for task_id, task in self._tasks.items():
    RuntimeError: dictionary changed size during iteration

Diagnose the root cause of this bug and provide a fix.

## Ground truth

**Root cause**: `cancel_all()` iterates directly over the live `self._tasks`
dict. Concurrently, each `worker()` coroutine's `finally` block calls
`manager._tasks.pop(task_id, None)` as it completes. If a worker's `finally`
block runs while `cancel_all()` is mid-iteration over that same dict (which
`await asyncio.sleep(0)` inside the loop makes likely, since it yields
control back to the event loop), the dict's size changes mid-iteration and
Python raises `RuntimeError`.

**Correct fix**: iterate over a snapshot, not the live dict:

```python
for task_id, task in list(self._tasks.items()):
    ...
```

This has been verified: the buggy version reproduces the RuntimeError
reliably (3/3 runs with the included random seed); the snapshot-based fix
was verified clean across 50/50 runs with the same parameters.

## What this tests

- Root-cause reasoning about concurrency/timing bugs, as opposed to surface
  pattern-matching on the exception type/message alone
- Whether the proposed fix introduces new issues (e.g. unjustified exception
  swallowing) or fabricates non-existent bugs elsewhere in the code

## Grading notes

- Pass = correct root-cause diagnosis (mutation during iteration over a
  shared dict from concurrent coroutines) and a fix that actually resolves it
  (snapshotting before iteration, or an equivalent restructuring).
- A fix that merely wraps the loop in `try/except RuntimeError: pass` should
  be flagged as treating the symptom, not the cause, and noted as a lesser
  pass even if it technically stops the crash.
- Hallucinations in auxiliary explanation (e.g. an incorrect claim about an
  unrelated API's behavior) are counted but don't disqualify the rank if the
  core fix is correct.
