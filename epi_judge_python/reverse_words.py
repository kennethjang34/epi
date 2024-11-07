import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a list of strings, each of which is of length 1, e.g.,
# ['r', 'a', 'm', ' ', 'i', 's', ' ', 'c', 'o', 's', 't', 'l', 'y'].
# each word is separated by ' '

# TC: O(n), n: len(s)
# the first for-loop reverses all the characters, but it will also reverse the characters within the same word.
# ex: "Alice likes Bob" becomes "boB sekil ecilA"
# Therefore, the characters within the same word should be revesred again.
def reverse_words(s: list[str]):
    for i in range(len(s) // 2):
        s[i], s[~i] = s[~i], s[i]
    i = 0
    while i < len(s):
        if s[i] == " ":
            i += 1
            continue
        else:
            j = i + 1
            while j < len(s) and s[j] != " ":
                j += 1
            for k in range((j - i) // 2):
                s[i + k], s[j - 1 - k] = s[j - 1 - k], s[i + k]
            i = j
    return s


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = list(s)

    executor.run(functools.partial(reverse_words, s_copy))

    return "".join(s_copy)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_words.py", "reverse_words.tsv", reverse_words_wrapper
        )
    )
