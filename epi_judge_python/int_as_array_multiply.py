from typing import List

from test_framework import generic_test


# TC: O(nm)
def multiply(num1: List[int], num2: List[int]) -> List[int]:
    sign = 1
    if num1[0] * num2[0] < 0:
        sign = -1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])
    n = len(num1)
    m = len(num2)
    # when multipling n digit number with m digit number,
    # the product can be at most n+m digits
    ans = [0] * (n + m)
    for i, d1 in reversed(list(enumerate(num1))):
        for j, d2 in reversed(list(enumerate(num2))):
            multiplied = d1 * d2
            ans[i + j + 1] += multiplied
            ans[i + j] += ans[i + j + 1] // 10
            ans[i + j + 1] = ans[i + j + 1] % 10
    # find the first non zero digit's index to remove leading zeros
    first_digit_idx = next((i for i, x in enumerate(ans) if x != 0), len(ans))
    ans = ans[first_digit_idx:] or [0]
    ans[0] *= sign
    return ans


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "int_as_array_multiply.py", "int_as_array_multiply.tsv", multiply
        )
    )
