from test_framework import generic_test


# TC: O(k) == O(log x), k: number of digits == floor(log(x,10)). 
def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    if x == 0:
        return True
    import math

    k = math.floor(math.log10(x))

    # v1 with temp var, x not changing

    # temp = x
    # for i in range(k // 2 + 1):
    #     rhs = temp % 10
    #     lhs = (x // (10 ** (k - i))) % 10
    #     temp //= 10
    #     if rhs != lhs:
    #         return False
    # return True

    # v2 without temp var, removing msd and lsd from x for each iteration
    msd_mask = 10 ** (k)
    for i in range(k // 2 + 1):
        rhs = x % 10
        lhs = x // msd_mask
        print(k, lhs, rhs)
        if rhs != lhs:
            return False
        x = x % msd_mask
        x = x // 10
        msd_mask = msd_mask // 100
    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_number_palindromic.py",
            "is_number_palindromic.tsv",
            is_palindrome_number,
        )
    )
