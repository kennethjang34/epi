from test_framework import generic_test


# TC: O(kn), SC: O(n), where n: number of total steps needed and k: maximum steps
def number_of_ways_to_top(top: int, maximum_step: int) -> int:
    mem = [1] + [0] * top
    for i in range(1, top + 1):
        for j in range(1, min(maximum_step + 1, i + 1)):
            mem[i] += mem[i - j]
    return mem[-1]


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "number_of_traversals_staircase.py",
            "number_of_traversals_staircase.tsv",
            number_of_ways_to_top,
        )
    )
