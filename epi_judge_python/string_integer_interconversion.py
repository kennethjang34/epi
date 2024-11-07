from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if x == 0:
        return "0"
    ans = []
    sign = 1
    if x < 0:
        sign = -1
        x *= -1
    while x > 0:
        next = x % 10
        ans.append(chr(next + ord("0")))
        x //= 10
    if sign < 0:
        ans.append("-")
    ans = "".join(reversed(ans))
    return ans


def string_to_int(s: str) -> int:
    sign = 1
    if s[0] == "+":
        s = s[1:]
    if s[0] == "-":
        sign = -1
        s = s[1:]
    ans = 0
    for c in s:
        int_c = ord(c) - ord("0")
        ans = 10 * ans + int_c
    ans = sign * ans
    return ans


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "string_integer_interconversion.py",
            "string_integer_interconversion.tsv",
            wrapper,
        )
    )
