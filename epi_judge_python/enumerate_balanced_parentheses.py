from typing import List

from test_framework import generic_test, test_utils


# TC: O((2k)!/((k!(k+1)!)))
def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    if num_pairs == 0:
        return [""]
    if num_pairs == 1:
        return ["()"]

    def helper(opened, right, cur):
        if right == 0:
            return [cur]
        if opened == right:
            for i in range(right):
                cur = cur + ")"
            return [cur]
        elif opened < right:
            ans = helper(opened + 1, right, cur + "(")
            if opened > 0:
                ans.extend(helper(opened - 1, right - 1, cur + ")"))
            return ans
        else:
            return []

    return helper(0, num_pairs, "")


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "enumerate_balanced_parentheses.py",
            "enumerate_balanced_parentheses.tsv",
            generate_balanced_parentheses,
            test_utils.unordered_compare,
        )
    )
