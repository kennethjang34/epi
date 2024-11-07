from test_framework import generic_test


def levenshtein_distance(A: str, B: str) -> int:
    # return levenshtein_distance_right_to_left(A, B)
    # return levenshtein_distance_left_to_right(A, B)
    return levenshtein_distance_bottom_top(A, B)


# TC, SC: O(len(A) * len(B))
def levenshtein_distance_bottom_top(A: str, B: str) -> int:
    table = [([(float("inf")) for _ in range(len(B) + 1)]) for _ in range(len(A) + 1)]
    for i in range(0, len(A) + 1):
        table[i][0] = i
    for j in range(0, len(B) + 1):
        table[0][j] = j
    for i in range(1, len(A) + 1):
        for j in range(len(B) + 1):
            a_p = A[i - 1]
            b_p = B[j - 1]
            if a_p == b_p:
                table[i][j] = table[i - 1][j - 1]
            else:
                table[i][j] = (
                    min(table[i - 1][j - 1], table[i - 1][j], table[i][j - 1]) + 1
                )
    return table[-1][-1]


# TC,SC: O(len(A) * len(B))
def levenshtein_distance_left_to_right(A: str, B: str) -> int:
    mem = [[-1 for _ in range(len(B))] for _ in range(len(A))]

    def helper(A, B, i, j):
        if min(len(A) - i, len(B) - j) <= 0:
            return max(len(A) - i, len(B) - j)
        if mem[i][j] != -1:
            return mem[i][j]
        ans = 0

        if A[i] == B[j]:
            ans = helper(A, B, i + 1, j + 1)
        else:
            cand_1 = helper(A, B, i, j + 1) + 1
            cand_2 = helper(A, B, i + 1, j + 1) + 1
            cand_3 = helper(A, B, i + 1, j) + 1
            ans = min(cand_1, cand_2, cand_3)
        mem[i][j] = ans
        return ans

    ans = helper(A, B, 0, 0)
    return ans


# TC,SC: O(len(A) * len(B))
def levenshtein_distance_right_to_left(A: str, B: str) -> int:
    mem = [[-1 for _ in range(len(B))] for _ in range(len(A))]

    def helper(A, B, i, j):
        if mem[i][j] != -1:
            return mem[i][j]
        if i < 0 or j < 0:
            return max(i, j) + 1
        ans = 0
        if A[i] == B[j]:
            ans = helper(A, B, i - 1, j - 1)
        else:
            cand_1 = helper(A, B, i - 1, j - 1) + 1
            cand_2 = helper(A, B, i - 1, j) + 1
            cand_3 = helper(A, B, i, j - 1) + 1
            ans = min(
                cand_1,
                cand_2,
                cand_3,
            )
        mem[i][j] = ans
        return ans

    ans = helper(A, B, len(A) - 1, len(B) - 1)
    return ans


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "levenshtein_distance.py", "levenshtein_distance.tsv", levenshtein_distance
        )
    )
