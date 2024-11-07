from test_framework import generic_test


# improved bute force, TC: O(k), k: number of bits set to 1 (assuming bit-wise operation takes O(1))
def count_bits(x: int) -> int:
    ans = 0
    while x != 0:
        ans += 1
        x &= x - 1
    return ans


if __name__ == "__main__":
    exit(generic_test.generic_test_main("count_bits.py", "count_bits.tsv", count_bits))
