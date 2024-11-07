from typing import List

from test_framework import generic_test




def helper(s: str, count=4, dp={}) -> List[str]:
    if (s, count) in dp:
        return dp[(s, count)]
    if count == 0:
        if len(s) == 0:
            return [""]
        else:
            return []
    cur = ""
    ans = []
    for i in reversed(range(max(len(s) - 4, 0), len(s))):
        c = s[i]
        int_v = (ord(c) - ord("0")) * (10 ** (len(s) - 1 - i))
        if cur == "" or int(cur) + int_v <= 255:
            cur = c + cur
            if len(cur) > 1 and cur[0] == "0":
                continue
            sub_res = helper(s[0:i], count - 1, dp=dp)
            ans.extend(
                [ss + "." + str(cur) if ss != "" else ss + str(cur) for ss in sub_res]
            )
    dp[(s, count)] = ans
    return ans


# TC: O(M^N * N), provided each integer is at most M digits and the input string is separated into N integers.
# Actually, since both M and N are constants (M=3, N=4), TC ~= O(3^4 * 4)
def get_valid_ip_address(s: str) -> List[str]:
    dp = {}
    res = helper(s=s, count=4, dp=dp)
    if res is None:
        return []
    return res


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "valid_ip_addresses.py",
            "valid_ip_addresses.tsv",
            get_valid_ip_address,
            comparator=comp,
        )
    )
