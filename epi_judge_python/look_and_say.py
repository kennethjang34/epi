from test_framework import generic_test


# TC: O(n*2^n) <- in reality, should be much better
# TC is very hard to calculate because it's a function of the lengths of encountered terms.
# However, each successive number can at most have 2 * # of digits of the previous number.
# This happens when all the digits of the previous number are different
# ex: 12345 -> 1112131415
# if previous number is 333344, then next number is just 4324, which is shorter than the previous #
def look_and_say(n: int) -> str:
    ans = []
    if n == 1:
        return "1"
    prev_seq = [1]
    prev_digit_count = 0
    for _ in range(2, n + 1):
        next_seq = []
        prev_digit = None
        prev_digit_count = 0
        for next_digit in prev_seq:
            if prev_digit is None:
                next_seq.append(next_digit)
            elif prev_digit != next_digit:
                next_seq.append(prev_digit_count)
                prev_digit_count = 0
                next_seq.append(next_digit)
            prev_digit_count += 1
            prev_digit = next_digit
        next_seq.append(prev_digit_count)
        ans = next_seq
        prev_seq = ans
    return "".join(str(x) for x in reversed(ans))


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "look_and_say.py", "look_and_say.tsv", look_and_say
        )
    )
