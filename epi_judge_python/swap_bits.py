from test_framework import generic_test


def brute_force(x, i, j):
    i_bit = (x >> i) & 1
    j_bit = (x >> j) & 1
    x = x & ~((1 << i) | 1 << j)
    return x | (j_bit << i) | (i_bit << j)


def check_diff(x, i, j):
    i_bit = (x >> i) & 1
    j_bit = (x >> j) & 1
    if i_bit ^ j_bit != 0:
        x ^= 1 << i | 1 << j
    return x


def swap_bits(x, i, j):
    # return brute_force(x, i, j)
    return check_diff(x, i, j)


if __name__ == "__main__":
    exit(generic_test.generic_test_main("swap_bits.py", "swap_bits.tsv", swap_bits))
