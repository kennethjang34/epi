from test_framework import generic_test
import collections


# TC: O(len(letter_text)+len(magazine_text))
def is_letter_constructible_from_magazine(letter_text: str, magazine_text: str) -> bool:
    let_counts = collections.Counter(letter_text)
    meg_counts = collections.Counter(magazine_text)
    diff = let_counts - meg_counts
    return len(diff) == 0


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_anonymous_letter_constructible.py",
            "is_anonymous_letter_constructible.tsv",
            is_letter_constructible_from_magazine,
        )
    )
