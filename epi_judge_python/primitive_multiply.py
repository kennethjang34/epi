from test_framework import generic_test


# helper function for addition, TC: O(n)
def add(x, y):
    and_bits = (x & y) << 1
    xor_bits = x ^ y
    if xor_bits & and_bits == 0:
        return xor_bits | and_bits
    else:
        return add(and_bits, xor_bits)


# TC: O(n^2) due to calling add(x,y), which has TC of O(n) n times in the worst case
def through_factoring(x: int, y: int) -> int:
    if x == 0 or y == 0:
        return 0
    if x == 1:
        return y
    if y == 1:
        return x
    ans = 0
    temp = y
    while temp != 0:
        if temp & 1:
            ans = add(ans, x)
            temp ^= 1
        else:
            x = x << 1
            temp = temp >> 1
    return ans


# TC: O(n^2) due to calling add(x,y), which has TC of O(n) n times in the worst case
def bit_by_bit(x: int, y: int) -> int:
    running_sum = 0
    while y > 0:
        if y & 1:
            running_sum = add(running_sum, x)
        x <<= 1
        y >>= 1
    return running_sum


def multiply(x: int, y: int) -> int:
    return bit_by_bit(x, y)
    # return through_factoring(x, y)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "primitive_multiply.py", "primitive_multiply.tsv", multiply
        )
    )
