import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# TC: O(2^n), n: number of bits
def gray_code(num_bits: int) -> List[int]:
    if num_bits == 0:
        return [0]
    if num_bits == 1:
        return [0, 1]
    elif num_bits == 2:
        return [0, 1, 3, 2]
    else:
        sub = gray_code(num_bits - 1)
        ans = []
        for i in [0, 1]:
            if i == 0:
                for c in sub:
                    ans.append(c)
            else:
                for c in sub[::-1]:
                    ans.append((1 << (num_bits - 1)) + c)
        return ans


def differ_by_1_bit(a, b):
    x = a ^ b
    if x == 0:
        return False
    while x & 1 == 0:
        x >>= 1
    return x == 1


@enable_executor_hook
def gray_code_wrapper(executor, num_bits):
    result = executor.run(functools.partial(gray_code, num_bits))

    expected_size = 1 << num_bits
    if len(result) != expected_size:
        raise TestFailure(
            "Length mismatch: expected "
            + str(expected_size)
            + ", got "
            + str(len(result))
        )
    for i in range(1, len(result)):
        if not differ_by_1_bit(result[i - 1], result[i]):
            if result[i - 1] == result[i]:
                raise TestFailure("Two adjacent entries are equal")
            else:
                raise TestFailure("Two adjacent entries differ by more than 1 bit")

    uniq = set(result)
    if len(uniq) != len(result):
        raise TestFailure(
            "Not all entries are distinct: found "
            + str(len(result) - len(uniq))
            + " duplicates"
        )


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "gray_code.py", "gray_code.tsv", gray_code_wrapper
        )
    )
