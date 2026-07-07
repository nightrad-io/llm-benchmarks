"""
P1 fixture: deterministic input array for the "Longest Consecutive Run" task,
plus an independently-implemented reference solution to verify any model's
output against.
"""
import random

random.seed(42)

# Deliberately unsorted, with duplicates, gaps, and one clear longest run
# embedded at scattered positions (tests value-based, not index-based, logic).
INPUT_ARRAY = [100, 4, 200, 1, 3, 2, 4, 50, 51, 52, 53, 50, 1000, -5, -4, -3]
random.shuffle(INPUT_ARRAY)

# Expected longest run: 1,2,3,4 -> length 4 (also 50,51,52,53 -> length 4; tie)
# Reference (independent, O(n) set-based) implementation:

def longest_consecutive_run(nums: list[int]) -> int:
    """Return the length of the longest run of consecutive integer VALUES
    present in nums, in O(n) time. Duplicates do not extend a run.
    Empty input returns 0. Order/position in the input is irrelevant."""
    if not nums:
        return 0
    num_set = set(nums)
    best = 0
    for n in num_set:
        if (n - 1) not in num_set:  # only start counting at a run's start
            length = 1
            while (n + length) in num_set:
                length += 1
            best = max(best, length)
    return best


if __name__ == "__main__":
    print("INPUT_ARRAY =", INPUT_ARRAY)
    result = longest_consecutive_run(INPUT_ARRAY)
    print("Reference answer (longest run length):", result)

    # Required test cases per the prompt
    assert longest_consecutive_run([]) == 0, "empty input failed"
    assert longest_consecutive_run([7]) == 1, "single element failed"
    assert longest_consecutive_run([5, 5, 5, 5]) == 1, "duplicates-only failed"
    assert longest_consecutive_run([1, 2, 2, 3]) == 3, "duplicates-within-run failed"
    print("All reference self-checks passed.")
