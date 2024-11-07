from typing import DefaultDict, List

from test_framework import generic_test


def find_all_substrings(s: str, words: List[str]) -> List[int]:
    return find_all_substrings_optimal(s, words)
    # return find_all_substrings_bf_very_slow(s, words)


def find_all_substrings_optimal(s: str, words: List[str]) -> List[int]:
    ans = []
    word_len = len(words[0])
    word_freq = collections.Counter(words)
    for l in range(len(s) - len(words) * word_len + 1):
        cur_freq = collections.Counter()
        flag = True
        for i in range(l, l + len(words) * word_len, word_len):
            cur_word = s[i : i + word_len]
            it = word_freq[cur_word]
            if it == 0:
                flag = False
                break
            else:
                cur_freq[cur_word] += 1
                if cur_freq[cur_word] > it:
                    flag = False
                    break
        if flag:
            ans.append(l)
    return ans


import collections


def helper(words, counts):
    counter = collections.Counter(words)
    if counter == counts:
        return True


# TC: O(n^2), SC: O(n)
def find_all_substrings_bf_very_slow(s: str, words: List[str]) -> List[int]:
    if len(s) < 1:
        return []
    word_len = len(words[0])
    bow = DefaultDict(int)
    for word in words:
        bow[word] += 1
    ans = []
    next_found = []
    for i in range(len(s) - word_len + 1):
        word = s[i : i + word_len]
        if word in bow:
            next_found.append(i)
    while len(next_found) != 0:
        l = next_found.pop(0)
        counts = bow.copy()
        r = l + word_len
        counter = 0
        while r <= len(s):
            word = s[l:r]
            counts[word] -= 1
            if counts[word] < 0:
                break
            else:
                counter += 1
            l = r
            r = l + word_len
        if counter == len(words):
            ans.append(l - word_len * (len(words)))
    return ans


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "string_decompositions_into_dictionary_words.py",
            "string_decompositions_into_dictionary_words.tsv",
            find_all_substrings,
        )
    )
