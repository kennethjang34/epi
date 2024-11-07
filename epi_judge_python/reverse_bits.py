from test_framework import generic_test


# bits must be a power of 2
# for the question itself, bits: 64, TC: O(n/2), n: number of bits (here 64)
def brute_force(x: int, bits: int) -> int:
    for lsb_pos in range(bits // 2):
        lsb = (x & (1 << lsb_pos)) >> lsb_pos
        msb_pos = bits - 1 - lsb_pos
        msb = (x & (1 << msb_pos)) >> msb_pos
        if lsb ^ msb == 1:
            x ^= (1 << msb_pos) | (1 << lsb_pos)
        else:
            continue
    return x


PRE_CALCULATED = None


# TC: O(n/l), n: number of bits (here assuming as constant of 64 though), l: subword size (here 16 bits)
def lookup(x: int) -> int:
    global PRE_CALCULATED
    if PRE_CALCULATED is None:
        PRE_CALCULATED = []
        for i in range(2**16):
            PRE_CALCULATED.append(brute_force(i, 16))
    return (
        PRE_CALCULATED[x >> 48]
        | PRE_CALCULATED[(x >> 32) & ((1 << 16) - 1)] << 16
        | (PRE_CALCULATED[(x >> 16) & ((1 << 16) - 1)] << 32)
        | (PRE_CALCULATED[x & ((1 << 16) - 1)] << 48)
    )


# Assume x is 64 bit unsigned int
def reverse_bits(x: int) -> int:
    return lookup(x)
    # return brute_force(x, 64)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "reverse_bits.py", "reverse_bits.tsv", reverse_bits
        )
    )
