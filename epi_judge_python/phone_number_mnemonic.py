from typing import List

from test_framework import generic_test, test_utils

MAPPING = ("0", "1", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ")


def phone_mnemonic(phone_number: str) -> List[str]:
    return phone_mnemonic_recursive(phone_number)
    # return phone_mnemonic_recursive_possibly_slower(phone_number)
    # return phone_mnemonic_iterative(phone_number)


# TC: O(4^n), SC: O(1) where n: number of digits in phone_number
def phone_mnemonic_iterative(phone_number: str) -> List[str]:
    ans = []
    if len(phone_number) == 0:
        return ans
    res = [""]
    for digit in phone_number:
        char_set = MAPPING[int(digit)]
        after_digit = []
        for c in char_set:
            for pre in res:
                after_digit.append(pre + c)
        res = after_digit
    return res


# TC: O(4^n), SC: O(n) where n: number of digits in phone_number
def phone_mnemonic_recursive(phone_number: str) -> List[str]:
    ans = []
    if len(phone_number) > 0:
        char_set = MAPPING[int(phone_number[0])]
        following = phone_mnemonic(phone_number[1:])
        for c in char_set:
            ans.extend([c + s for s in following])
    else:
        ans.append("")
    return ans


# TC: O(n* 4^n), SC: O(n) where n: number of digits in phone_number
def phone_mnemonic_recursive_possibly_slower(phone_number: str) -> List[str]:
    def helper(digit: int):
        if digit == len(phone_number):
            mnemonics.append("".join(partial_mnemonic))
        else:
            for c in MAPPING[int(phone_number[digit])]:
                partial_mnemonic[digit] = c
                helper(digit + 1)

    mnemonics = []
    partial_mnemonic = ["0"] * len(phone_number)
    helper(0)
    return mnemonics


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "phone_number_mnemonic.py",
            "phone_number_mnemonic.tsv",
            phone_mnemonic,
            comparator=test_utils.unordered_compare,
        )
    )
