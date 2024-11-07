from math import inf
from typing import List

from test_framework import generic_test


def brute_force(prices: List[float]) -> float:
    ans = 0
    n = len(prices)
    for i, cp in enumerate(prices):
        first_max = 0
        for j in range(i + 1, n):
            fp = prices[j]
            if first_max < fp - cp:
                first_max = fp - cp
                second_max = 0
                for p in range(j + 1, n):
                    cp2 = prices[p]
                    for q in range(p + 1, n):
                        fp2 = prices[q]
                        if second_max < fp2 - cp2:
                            second_max = fp2 - cp2
                if ans < first_max + second_max:
                    ans = first_max + second_max
    return ans


# TC: O(n), SC: O(n)
# First,calculate maximum profits obtainable  by selling before or on day i, saving result in first_max_profits[i]
# Second, iterate through the prices in reversed order with index j, storing the maximum price encountered upto now.
# Assume second buying  happens on day j. then max profit from the second buy-sell is: max_price - prices[j]
# first buy-sell max profit that could happen before or on day j has already been calculated and stored in first_max_profits[j].
# Therefore,  max_profit = max(max_profit, first_max_profits[i] + max_price - p) results in max profit from at most two buying-selling
def dp_with_extra_mem(prices: List[float]) -> float:
    n = len(prices)
    first_max_profits = [0.0] * n
    max_profit = 0.0
    buy = prices[0]
    for i, p in enumerate(prices):
        max_profit = max(max_profit, p - buy)
        first_max_profits[i] = max_profit
        if p < buy:
            buy = p
    max_price = 0
    for i in reversed(list(range(0, n))):
        p = prices[i]
        max_price = max(p, max_price)
        max_profit = max(max_profit, first_max_profits[i] + max_price - p)
    return max_profit


# TC: O(n), SC: O(1)
def dp_without_extra_mem(prices: List[float]) -> float:
    first_buy = inf
    after_first_sell = 0
    after_second_buy = -inf
    after_second_sell = -inf
    for p in prices:
        first_buy = min(first_buy, p)
        after_first_sell = max(after_first_sell, p - first_buy)
        after_second_buy = max(after_second_buy, after_first_sell - p)
        after_second_sell = max(after_second_sell, after_second_buy + p)
    return after_second_sell


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    # return brute_force(prices=prices)
    # return dp_with_extra_mem(prices=prices)
    return dp_without_extra_mem(prices=prices)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "buy_and_sell_stock_twice.py",
            "buy_and_sell_stock_twice.tsv",
            buy_and_sell_stock_twice,
        )
    )
