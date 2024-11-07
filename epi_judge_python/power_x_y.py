from test_framework import generic_test


# TC: O(2^n), n: number of bits used for representing y
def brute_force(x: float, y: int) -> float:
    result = 1
    neg = False
    if y < 0:
        neg = True
        y = -y
    for _ in range(y):
        result = result * x
    if neg is True:
        return 1 / result
    else:
        return result


#TC: O(n), n: number of bits used for representing y
def optimized(x: float, y: int) -> float:
    if y == 0:
        return 1
    neg = False
    if y < 0:
        neg = True
        y = -y
    result = 1
    cur = x
    power = 0
    while y > 0:
        if y & (1 << power) != 0:
            result = result * cur
            y -= 1 << power
        power += 1
        cur = cur * cur

    if neg is True:
        return 1 / result
    else:
        return result


# Q: get x^y
def power(x: float, y: int) -> float:
    # return brute_force(x, y)
    return optimized(x, y)


if __name__ == "__main__":
    exit(generic_test.generic_test_main("power_x_y.py", "power_x_y.tsv", power))
