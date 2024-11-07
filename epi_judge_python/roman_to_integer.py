from test_framework import generic_test
import functools

T = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


# TC: O(n)
def left_to_right(s: str) -> int:
    ans = 0
    i = 0
    while i < len(s):
        rd = s[i]
        n = T[rd]
        if i != len(s) - 1:
            # although method is checking each exception, it doesn't need to check them.
            # instead, checking whether the next digit is bigger and if so, subtract the current one from running sum
            # this is because input string s is assumed to be valid
            if rd == "I" and s[i + 1] in ("V", "X"):
                n = T[s[i + 1]] - T[rd]
                i += 1
            if rd == "X" and s[i + 1] in ("L", "C"):
                n = T[s[i + 1]] - T[rd]
                i += 1
            if rd == "C" and s[i + 1] in ("D", "M"):
                n = T[s[i + 1]] - T[rd]
                i += 1
        ans += n
        i += 1
    return ans


# TC: O(n). 
# Almost the same as left_to_right version but easier to code.
# this method doesn't check each exception but just subtract value for s[i] if it's less than value for s[i+1]
# Given "IC", return 99. "IC" is roman number but inputs are assumed to be valid so it doesn't matter
def right_to_left(s: str) -> int:
    return functools.reduce(
        lambda cumul, i: cumul + (-T[s[i]] if T[s[i]] < T[s[i + 1]] else T[s[i]]),
        reversed(range(len(s) - 1)),
        T[s[-1]],
    )


def roman_to_integer(s: str) -> int:
    # return left_to_right(s)
    return right_to_left(s)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", "roman_to_integer.tsv", roman_to_integer
        )
    )
