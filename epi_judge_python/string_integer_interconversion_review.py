from test_framework import generic_test
from test_framework.test_failure import TestFailure
import sys


def get_digit_str(n):
    return chr(ord("0") + n)


def get_digit_int(n):
    return ord(n) - ord("0")


sys.setrecursionlimit(15000)


def int_to_string(x: int) -> str:
    if x // 10 == 0:
        return get_digit_str(x)
    else:
        sgn = ""
        if x < 0:
            sgn = "-"
            x = -x
        ans = ""
        e = 0
        while x != 0:
            ans = get_digit_str(x % 10) + ans
            x //= 10
            e += 1
        return sgn + ans


def string_to_int(s: str) -> int:
    if len(s) == 0:
        return 0
    else:
        sgn = 1
        if s[0] == "-":
            sgn = -1
        temp = s
        idx = 0
        while idx < len(temp) and (
            temp[idx] == "0" or temp[idx] == "+" or temp[idx] == "-"
        ):
            idx += 1
        digits_only = temp[idx:]
        if len(digits_only) == 0:
            return 0
        ans = 0
        for j in range(len(digits_only)):
            e = len(digits_only) - j - 1
            d = digits_only[j]
            ans += get_digit_int(d) * (10 ** (e))
        ans = sgn * ans
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
