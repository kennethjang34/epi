from typing import List

from test_framework import generic_test


# iterate through all the future prices after buying on day i.
# TC: O(n^2), SC: O(1)
def brute_force(prices: List[float]) -> float:
    running_max = 0
    for i, cp in enumerate(prices):
        for j, fp in enumerate(prices[i + 1 :]):
            running_max = max(running_max, fp - cp)

    return running_max


# divide input array into 2 halves and calculate return the maximum profit of sub-maximum profits
# that can be obtained within the first,second halves and (max pricefrom the second half - min pricefrom the first half)
# TC: O(n*log(n))
def divide_and_conquer(prices: List[float]) -> float:
    n = len(prices)
    if n < 2:
        return 0
    elif n == 2:
        max(prices[1] - prices[0], 0)
    first = divide_and_conquer(prices=prices[: n // 2])
    second = divide_and_conquer(prices=prices[n // 2 :])
    # if max profit can be obtained buying in one half and selling in the other half, the buying should happen in the first half and selling in the second
    min_left = min(prices[: n // 2])
    max_right = max(prices[n // 2 :])
    return max(first, second, max_right - min_left)


# iterate through input prices only once,
# considering that for maximum profit's buy day, there should be no previous days with lower prices
# TC: O(n), SC: O(1)
def optimized(prices: List[float]) -> float:
    running_max = 0
    buy = prices[0]
    for i, cp in enumerate(prices[1:]):
        if buy > cp:
            buy = cp
        running_max = max(running_max, cp - buy)
    return running_max


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # return brute_force(prices=prices)
    # return divide_and_conquer(prices=prices)
    return optimized(prices)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "buy_and_sell_stock.py", "buy_and_sell_stock.tsv", buy_and_sell_stock_once
        )
    )
