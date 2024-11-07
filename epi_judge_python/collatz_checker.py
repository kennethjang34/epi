from test_framework import generic_test


def test_collatz_conjecture(n: int) -> bool:
    return test_collatz_conjecture_1(n)
    # return test_collatz_conjecture_2(n)


# O(n)..?
def test_collatz_conjecture_1(n: int) -> bool:
    if n < 1:
        return False
    mem = set([1, 2])
    for i in range(3, n + 1):
        if i not in mem:
            x = i
            encountered = set()
            while x >= i:
                if x in encountered:
                    return False
                encountered.add(x)
                mem.add(x)
                if x in mem:
                    break
                if x % 2 == 0:
                    x = x // 2
                else:
                    x = x * 3 + 1
    return n in mem


# O(n)..?
def test_collatz_conjecture_2(n: int) -> bool:
    verified_numbers = set()
    for i in range(3, n + 1):
        sequence = set()
        test_i = i
        while test_i >= i:
            if test_i in sequence:
                return False
            sequence.add(test_i)
            if test_i % 2:
                if test_i in verified_numbers:
                    break
                verified_numbers.add(test_i)
                test_i = 3 * test_i + 1
            else:
                test_i //= 2
    return True


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "collatz_checker.py", "collatz_checker.tsv", test_collatz_conjecture
        )
    )
