# P1: Algorithm Correctness — "Longest Consecutive Run"

Concrete, verified fixture. Run `python3 fixture_generator.py` in this folder
to print the exact input array and the reference answer.

## Prompt

Write a function to find the longest run of consecutive integers in the
following unsorted list:

    [50, 52, 2, 4, -4, 53, 1000, 51, 4, 200, -5, -3, 3, 50, 100, 1]

Requirements:
- O(n) time complexity
- Include a docstring
- Include test cases covering: empty input, duplicates, and a single element

Note: "consecutive integers" means consecutive *values* (e.g. [4, 2, 1, 3] has
a run of length 4: 1,2,3,4), regardless of their position/order in the input
array — not array-index adjacency (LeetCode 128 style).

## Ground truth

Longest run length = **4**. There are two runs of equal length in this
fixture: [1, 2, 3, 4] and [50, 51, 52, 53]. Either is an acceptable correct
answer for "the longest run length"; a model citing one specific run as *the*
longest (rather than noting the tie) is not penalized, since the prompt asks
for the length, not enumeration of all maximal runs.

## What this tests

- Algorithmic correctness and problem comprehension (does the model correctly
  interpret "unsorted list" as a signal for the value-based interpretation
  rather than array-adjacency?)
- Whether self-generated test suites are actually correct (several models in
  the original run wrote tests that would crash or report false failures)

## Grading notes

- Pass = the core deliverable (the function) is correct, returns 4 on the
  fixture input above, and is verifiably O(n).
- Hallucinations in *auxiliary* code (e.g. a broken test assertion alongside
  an otherwise-correct function) are counted but do not disqualify the rank,
  since the primary deliverable is independently verifiable and correct on
  its own.

See `fixture_generator.py` for the reference O(n) implementation and required
test-case assertions (empty, single-element, duplicates-only,
duplicates-within-a-run).
