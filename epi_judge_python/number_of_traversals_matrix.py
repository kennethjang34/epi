from test_framework import generic_test


# TC, SC: O(n * m)
def number_of_ways(n: int, m: int) -> int:
    table = [[0] * (m) for _ in range(n)]

    def helper(n, m, table):
        down = n - 1
        right = m - 1
        if down == 0 or right == 0:
            return 1
        elif table[down][right]:
            return table[down][right]
        else:
            ans = helper(n - 1, m, table) + helper(n, m - 1, table)
            table[down][right] = ans
            return ans

    return helper(n, m, table)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "number_of_traversals_matrix.py",
            "number_of_traversals_matrix.tsv",
            number_of_ways,
        )
    )
