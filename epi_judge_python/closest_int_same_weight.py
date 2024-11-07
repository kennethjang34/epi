from test_framework import generic_test


# TC: O(n)
def brute_force(x: int) -> int:
    temp = x
    while temp != 0:
        candidate = temp & ~(temp - 1)
        if candidate != 1 and x & (candidate >> 1) == 0:
            return (x ^ candidate) | (candidate >> 1)
        elif x & (candidate << 1) == 0:
            return (x ^ candidate) | (candidate << 1)

        temp ^= candidate
    return x | (x + 1)


# TC: O(1)
def constant_tc(x: int) -> int:
    lowest_set_bit = x & ~(x - 1)
    lowest_unset_bit = ~x & (x + 1)
    if lowest_set_bit >= lowest_unset_bit:
        x = (x ^ lowest_set_bit) | (lowest_set_bit >> 1)
    else:
        x = (x ^ (lowest_unset_bit >> 1)) | lowest_unset_bit
    return x


def closest_int_same_bit_count(x: int) -> int:
    # return brute_force(x)
    return constant_tc(x)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "closest_int_same_weight.py",
            "closest_int_same_weight.tsv",
            closest_int_same_bit_count,
        )
    )
