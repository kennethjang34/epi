from test_framework import generic_test


# improved brute force TC: O(k), k: number of set bits
def improved_brute_force(x: int) -> int:
    res = 0
    while x != 0:
        res ^= 1
        x = x & (x - 1)
    return res


# TC: O(n), n: word size
def brute_force(x: int) -> int:
    res = 0
    while x != 0:
        res ^= x & 1
        x >>= 1
    return res


PRE_CALCULATED = None


# assuming word size: 8 bytes= 64 bits,
# we can cache subword of size 2 bytes = 16 bits
# TC: O(n/l), n: word size, l: subword size used as index for PRE_CALCULATED cache
def cache(x: int) -> int:
    global PRE_CALCULATED
    if PRE_CALCULATED is None:
        PRE_CALCULATED = []
        for i in range(0, 2**16):
            parity = 0
            while i != 0:
                parity ^= 1
                i &= i - 1
            PRE_CALCULATED.append(parity)
    bit_mask = 0xFFFF
    mask_size = 16
    res = (
        PRE_CALCULATED[x >> (mask_size * 3)]
        ^ PRE_CALCULATED[(x >> (mask_size * 2)) & bit_mask]
        ^ PRE_CALCULATED[(x >> (mask_size * 1)) & bit_mask]
        ^ PRE_CALCULATED[x & bit_mask]
    )
    return res


# using xor's properties:
# 1. xor operation is commutative: 10 ^ 11 = (1^1)<<1 + (0^1)<<0 == (0^1)<<0 + (1^1)<<1
# 2. xor operation is associative: 11 ^ 10 ^ 01 == 10 ^ 11 ^ 01
# TC: O(log n), n: word size
def xor_commutative_associative(x: int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1


def parity(x: int) -> int:
    # return brute_force(x)
    # return improved_brute_force(x)
    # return cache(x)
    return xor_commutative_associative(x)


if __name__ == "__main__":
    exit(generic_test.generic_test_main("parity.py", "parity.tsv", parity))
