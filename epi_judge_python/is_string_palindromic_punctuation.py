from test_framework import generic_test


# TC: O(n)
def is_palindrome(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i <= j:
        a = s[i]
        if a.isalnum() is False:
            i += 1
            continue
        b = s[j]
        if b.isalnum() is False:
            j -= 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_palindromic_punctuation.py",
            "is_string_palindromic_punctuation.tsv",
            is_palindrome,
        )
    )
