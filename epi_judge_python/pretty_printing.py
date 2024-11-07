from typing import List

from test_framework import generic_test


# TC: O(kn), SC: O(n), where k: line length and n: number of words
def minimum_messiness(words: List[str], line_length: int) -> int:
    def helper(words, end, line_length, mem):
        if end in mem:
            return mem[end]
        elif end < 0:
            return 0
        else:
            i = end
            word = words[i]
            left = line_length
            messiness = float("inf")
            while i >= 0 and (left - len(words[i]) - (0 if (end == i) else 1)) >= 0:
                word = words[i]
                left -= len(word) + (0 if (end == i) else 1)
                predecessor = helper(words, i - 1, line_length, mem)
                cur_messiness = left**2
                messiness = min(cur_messiness + predecessor, messiness)
                i -= 1
            mem[end] = messiness
            return messiness

    mem = {}
    res = helper(words, len(words) - 1, line_length, mem)
    return res


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "pretty_printing.py", "pretty_printing.tsv", minimum_messiness
        )
    )
