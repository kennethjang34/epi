from collections import defaultdict
from test_framework import generic_test


## V1:
# TC: O(n), SC: O(number of distinct characters in input string)
def can_form_palindrome_v1(s: str) -> bool:
    counts = defaultdict(int)
    for c in s:
        counts[c] += 1
    odd_allowed = len(s) % 2
    for count in counts.values():
        if count % 2 != 0:
            odd_allowed -= 1
            if odd_allowed < 0:
                return False
    return True


## V2:
# TC: O(n), SC: O(number of distinct characters in input string)
def can_form_palindrome_v2(s: str) -> bool:
    import collections

    counts = collections.Counter(s).values()
    return sum(count % 2 for count in counts) < 2


def can_form_palindrome(s: str) -> bool:
    # return can_form_palindrome_v1(s)
    return can_form_palindrome_v2(s)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_permutable_to_palindrome.py",
            "is_string_permutable_to_palindrome.tsv",
            can_form_palindrome,
        )
    )
