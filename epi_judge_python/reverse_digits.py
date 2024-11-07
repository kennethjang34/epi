from test_framework import generic_test


# TC: O(k) == O(log x), k: floor(log x), SC: O(1)
# faster than with vec due to fewer memory read
def without_vec(x: int) -> int:
    res = 0
    sign = 1
    if x < 0:
        sign = -1
        x = -x
    while x > 0:
        res = res * 10 + x % 10
        x //= 10
    return res * sign


# TC: O(k) == O(log x), k: floor(log x), SC: O(k) == O(log x)
def brute_force(x: int) -> int:
    l = []
    sign = 1
    if x < 0:
        sign = -1
        x = -x
    while x > 0:
        l.append(x % 10)
        x //= 10
    k = len(l) - 1
    res = 0
    for i in range(k + 1):
        res += l[i] * (10 ** (k - i))
    return res * sign


def reverse(x: int) -> int:
    # return brute_force(x)
    return without_vec(x)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_digits.py", "reverse_digits.tsv", reverse
        )
    )
