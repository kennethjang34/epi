from typing import List

from test_framework import generic_test


def palindrome_decompositions(text: str) -> List[List[str]]:
    # return palindrome_decompositions_shorter_v(text)
    return palindrome_decompositions_recursive(text)


# TC: O(n * 2^n) in worst case (when the input string consists of n repetitions of a single character).
def palindrome_decompositions_recursive(text: str) -> List[List[str]]:
    parts: List[List[str]] = []

    def is_palindromic(chars: List[str]):
        if len(chars) <= 1:
            return True
        if chars[0] != chars[-1]:
            return False
        if len(chars) % 2 == 1:
            return is_palindromic(chars[1:-1])
        else:
            return is_palindromic(chars[1:-1])

    def helper(chars: List[str], cur: List[List[str]], parts: List[List[str]]):
        if len(chars) == 0:
            components = ["".join(char_list) for char_list in cur if len(char_list) > 0]
            parts.append(components)
        else:
            cur.append([])
            for i, c in enumerate(chars):
                candidate = cur[-1]
                candidate.append(c)
                if is_palindromic(candidate):
                    helper(chars[i + 1 :], cur, parts)
            cur.pop(-1)

    helper([c for c in text], [], parts)

    return parts


# TC: O(n * 2^n) in worst case (when the input string consists of n repetitions of a single character).
def palindrome_decompositions_shorter_v(text: str) -> List[List[str]]:
    if text == "":
        return [[]]
    else:
        res = []
        for i in range(1, len(text) + 1):
            if text[:i] == text[:i][::-1]:
                for right in palindrome_decompositions_shorter_v(text[i:]):
                    res.append([text[:i]] + right)
        return res


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "enumerate_palindromic_decompositions.py",
            "enumerate_palindromic_decompositions.tsv",
            palindrome_decompositions,
            comp,
        )
    )
