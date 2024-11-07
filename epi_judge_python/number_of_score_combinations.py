from collections import defaultdict
from typing import List

from test_framework import generic_test


def num_combinations_for_final_score(
    final_score: int, individual_play_scores: List[int]
) -> int:
    # return num_combinations_for_final_score_recursive(
    #     final_score,
    #     individual_play_scores,
    # )
    # return num_combinations_for_final_score_iterative_non_optimal(
    #     final_score,
    #     individual_play_scores,
    # )
    return num_combinations_for_final_score_iterative_optimal(
        final_score,
        individual_play_scores,
    )


# TC: O(s^2 * n), SC: O(sn)
def num_combinations_for_final_score_iterative_non_optimal(
    final_score: int, individual_play_scores: List[int]
) -> int:
    table = [[1] + [0] * final_score for _ in individual_play_scores]
    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            k = 0
            score = individual_play_scores[i]
            while k * score <= j:
                table[i][j] += table[i - 1][j - k * score]
                k += 1
    return table[-1][-1]


# TC, SC: O(sn), s: number of score types, n: final score
def num_combinations_for_final_score_iterative_optimal(
    final_score: int, individual_play_scores: List[int]
) -> int:
    table = [[1] + [0] * final_score for _ in individual_play_scores]
    for i in range(len(individual_play_scores)):
        for j in range(1, final_score + 1):
            score = individual_play_scores[i]
            without_score = (table[i - 1][j]) if i >= 1 else 0
            with_score = (table[i][j - score]) if j >= score else 0
            table[i][j] = with_score + without_score
    return table[-1][-1]


def num_combinations_for_final_score_recursive(
    final_score: int, individual_play_scores: List[int], mem=None
):
    if mem is None:
        mem = [{} for _ in range(final_score + 1)]
    tupled = tuple(individual_play_scores)
    if final_score == 0:
        return 1
    if final_score < 0 or len(individual_play_scores) == 0:
        return 0
    if tupled in mem[final_score]:
        return mem[final_score][tupled]
    ans = 0
    score = individual_play_scores[0]
    without_score = individual_play_scores[1:]
    i = 0
    while final_score - i * score >= 0:
        if final_score == i * score:
            ans += 1
        else:
            sub_res = num_combinations_for_final_score_recursive(
                final_score - i * score, without_score, mem
            )
            ans += sub_res
        i += 1
    mem[final_score][tupled] = ans
    return ans


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "number_of_score_combinations.py",
            "number_of_score_combinations.tsv",
            num_combinations_for_final_score,
        )
    )
