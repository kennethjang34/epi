from typing import List

from test_framework import generic_test


def maximum_revenue(coins: List[int]) -> int:
    mem = {}
    # return max(
    #     maximum_revenue_designated_move(coins, True, mem, 0, len(coins)),
    #     maximum_revenue_designated_move(coins, False, mem, 0, len(coins)),
    # )
    # return max(
    #     maximum_revenue_recursive_sum_first(coins, mem, 0, len(coins)),
    #     maximum_revenue_recursive_sum_first(coins, mem, 0, len(coins)),
    # )
    return max(
        maximum_revenue_recursive_optimal(coins, mem, 0, len(coins)),
        maximum_revenue_recursive_optimal(coins, mem, 0, len(coins)),
    )

# TC: O(n^2), as there can be at most O(n^2) (i,j) pairs and each function call fills one entry at a time.
def maximum_revenue_recursive_optimal(coins: List[int], mem, i, j) -> int:
    if i >= j:
        return 0
    if (i, j) in mem:
        return mem[(i, j)]
    else:
        first_picked = coins[i] + min(
            maximum_revenue_recursive_optimal(coins, mem, i + 2, j),
            maximum_revenue_recursive_optimal(coins, mem, i + 1, j - 1),
        )
        last_picked = coins[j - 1] + min(
            maximum_revenue_recursive_optimal(coins, mem, i + 1, j - 1),
            maximum_revenue_recursive_optimal(coins, mem, i, j - 2),
        )
        ans = max(first_picked, last_picked)
        mem[(i, j)] = ans
        return ans



# TC: O(n^3), as there can be at most O(n^2) (i,j) pairs and there is O(n) operations for summing up the coins[i:j] at a time.
def maximum_revenue_recursive_sum_first(coins: List[int], mem, i, j) -> int:
    if i >= j:
        return 0
    if (i, j) in mem:
        return mem[(i, j)]
    else:
        total = sum(coins[i:j])
        if total - maximum_revenue_recursive_sum_first(
            coins, mem, i + 1, j
        ) >= total - maximum_revenue_recursive_sum_first(coins, mem, i, j - 1):
            ans = total - maximum_revenue_recursive_sum_first(coins, mem, i + 1, j)
        else:
            ans = total - maximum_revenue_recursive_sum_first(coins, mem, i, j - 1)
        mem[(i, j)] = ans
        return ans


# TC: O(2*(n^2)), as there are at most  O(n^2) (i,j) pairs with 2 possible first value
# argument first: represents whether or not the next player chooses the first or last coin.
def maximum_revenue_designated_move(coins: List[int], first, mem, i, j) -> int:
    if i >= j:
        return 0
    if (i, j, first) in mem:
        return mem[(i, j, first)]
    else:
        ans = 0
        if first:
            ans = coins[i]
            if maximum_revenue_designated_move(
                coins, True, mem, i + 1, j
            ) <= maximum_revenue_designated_move(coins, False, mem, i + 1, j):
                ans += max(
                    maximum_revenue_designated_move(coins, True, mem, i + 1, j - 1),
                    maximum_revenue_designated_move(coins, False, mem, i + 1, j - 1),
                )
            else:
                ans += max(
                    maximum_revenue_designated_move(coins, True, mem, i + 2, j),
                    maximum_revenue_designated_move(coins, False, mem, i + 2, j),
                )
        else:
            ans = coins[j - 1]
            if maximum_revenue_designated_move(
                coins, True, mem, i, j - 1
            ) <= maximum_revenue_designated_move(coins, False, mem, i, j - 1):
                ans += max(
                    maximum_revenue_designated_move(coins, True, mem, i, j - 2),
                    maximum_revenue_designated_move(coins, False, mem, i, j - 2),
                )
            else:
                ans += max(
                    maximum_revenue_designated_move(coins, True, mem, i + 1, j - 1),
                    maximum_revenue_designated_move(coins, False, mem, i + 1, j - 1),
                )
        mem[(i, j, first)] = ans
        return ans


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "picking_up_coins.py", "picking_up_coins.tsv", maximum_revenue
        )
    )
