import functools
from typing import Dict, List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain: str, dictionary: Set[str]) -> List[str]:
    # return decompose_into_dictionary_words_recursive(domain, dictionary)
    return decompose_into_dictionary_words_iterative(domain, dictionary)


# TC: O(n^3), SC: O(n), where n is length of domain
def decompose_into_dictionary_words_recursive(
    domain: str, dictionary: Set[str]
) -> List[str]:
    table = {}

    def helper(s: str, dictionary, table: Dict, i) -> List[str]:
        if i in table:
            return table[i]
        elif len(s) == i:
            return []
        for word in dictionary:
            if len(s) - i >= len(word) and s[i : i + len(word)] == word:
                sub = helper(s, dictionary, table, i + len(word))
                if sub is not None:
                    sub.append(word)
                    table[i] = sub
                    return sub
        table[i] = None
        return None

    ans = helper(domain, dictionary, table, 0)
    if ans is not None:
        ans.reverse()
        return ans
    else:
        return []

# TC: O(n^3), SC: O(n^2), where n is length of domain
# SC can be reduced to O(n), since we don't have to store the prefix words but their indicies/lengths
def decompose_into_dictionary_words_iterative(
    domain: str, dictionary: Set[str]
) -> List[str]:
    table: Dict[int, list] = {}
    table[0] = []
    for i in range(len(domain)):
        if i in table:
            for word in dictionary:
                prefix_words = table[i]
                if (i + len(word)) not in table:
                    if (
                        len(domain) >= i + len(word)
                        and domain[i : i + len(word)] == word
                    ):
                        prefix_words = prefix_words.copy()
                        prefix_words.append(word)
                        table[i + len(word)] = prefix_words
    return table[len(domain)] if len(domain) in table else []


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary, decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary)
    )

    if not decomposable:
        if result:
            raise TestFailure("domain is not decomposable")
        return

    if any(s not in dictionary for s in result):
        raise TestFailure("Result uses words not in dictionary")

    if "".join(result) != domain:
        raise TestFailure("Result is not composed into domain")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_string_decomposable_into_words.py",
            "is_string_decomposable_into_words.tsv",
            decompose_into_dictionary_words_wrapper,
        )
    )
