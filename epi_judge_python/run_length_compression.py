from test_framework import generic_test
from test_framework.test_failure import TestFailure


# TC: O(n)
# Note: digit part doesn't have to consist of a single digit ! (ex. 16h4b)
def decoding(s: str) -> str:
    ans = []
    i = 0
    while i < len(s):
        j = i + 1
        count = int(s[i])
        while j < len(s) and s[j].isdigit():
            count = 10 * count + int(s[j])
            j += 1
        ch = s[j]
        i = j + 1
        for _ in range(count):
            ans.append(ch)
    return "".join(ans)


# TC: O(n)
def encoding(s: str) -> str:
    if len(s) == 0:
        return ""
    ans = []
    i = 0
    while i < len(s):
        ch = s[i]
        j = i + 1
        while j < len(s) and s[j] == ch:
            j += 1
        ans.append(str(j - i))
        ans.append(ch)
        i = j
    return "".join(ans)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure("Decoding failed")
    if encoding(decoded) != encoded:
        raise TestFailure("Encoding failed")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "run_length_compression.py", "run_length_compression.tsv", rle_tester
        )
    )
