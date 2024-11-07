from test_framework import generic_test


# TC: O(n*m), where n: len(t), m: len(s). Given m <= n, TC roughly translates O(n^2)
# t: text, s: search string
def brute_force_search(t: str, s: str) -> int:
    if len(s) > len(t):
        return -1
    i = 0
    while i < len(t):
        j = i
        while j < len(t) and j - i < len(s):
            if t[j] == s[j - i]:
                j += 1
            else:
                break
        if j - i == len(s):
            return i
        i += 1
    return -1


# text search using Rabin-Karp  algorithm
# TC: O(n+m), where n: len(t), m: len(s),  provided proper hash function.
# Int type size matters because the method does not use modulus! (no hash conflict but very big int size)
# Considering m <= n, TC roughly translates O(n),
# t: text, s: search string
def rabin_karp(t: str, s: str) -> int:
    if len(s) > len(t):
        return -1
    base = 26
    t_hash = 0
    s_hash = 0
    power_s = base ** max(len(s) - 1, 0)
    if t[: len(s)] == s:
        return 0
    for i in range(len(s)):
        t_hash = t_hash * base + (ord(t[len(s) - 1 - i]))
    for i in range(len(s)):
        s_hash = s_hash * base + (ord(s[len(s) - 1 - i]))
    for i in range(1, len(t) - len(s) + 1):
        t_hash = (t_hash - (ord(t[i - 1]))) // base + power_s * (ord(t[i + len(s) - 1]))
        if t_hash == s_hash:
            return i
    return -1


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "substring_match.py", "substring_match.tsv", rabin_karp
        )
    )
