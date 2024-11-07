from test_framework import generic_test

# TC: O(n*log_b2(b1))
# O(n) multiply-and-adds for initial conversion of digit string into int value x, followed by
# O(log_b2(x)) multiply-and-adds for converting x into digit string in base b2.
# Since x is upperbounded by b1^n, O(log_b2(x)) => O(log_b2(b1^n)) => O(n*log_b2(b1))
def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    if num_as_string == "0":
        return "0"
    if num_as_string[0] == "-":
        sign = -1
        num_as_string = num_as_string[1:]
    else:
        sign = 1
    int_val = 0
    for d in num_as_string:
        next_val = ord(d) - ord("0")
        if next_val > 9 or next_val < 0:
            next_val = ord(d) - ord("A") + 10

        int_val = int_val * b1 + next_val
    ans = []
    while int_val > 0:
        next_val = int_val % b2
        if next_val < 10:
            next_digit = chr(next_val + ord("0"))
        else:
            next_digit = chr(next_val - 10 + ord("A"))
        ans.append(next_digit)
        int_val //= b2
    if sign < 0:
        ans.append("-")
    return "".join(reversed(ans))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "convert_base.py", "convert_base.tsv", convert_base
        )
    )
