from test_framework import generic_test


## assuming y >= 1 && 0<= x < 2^32
# TC: O(n), n: size of word (we are assuming n=32 though)
def divide(x: int, y: int) -> int:
    quotient = 0
    power = 31
    y_raised = y << power
    while x >= y:
        y_raised = y << power
        while x < y_raised:
            power -= 1
            y_raised = y << power
        x -= y_raised
        quotient += 1 << power
    return quotient


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "primitive_divide.py", "primitive_divide.tsv", divide
        )
    )
