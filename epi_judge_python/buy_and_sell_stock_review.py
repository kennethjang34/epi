from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # return buy_and_sell_stock_once_recursive(prices)
    # return buy_and_sell_stock_once_iter(prices)
    return buy_and_sell_stock_once_opt(prices)


def buy_and_sell_stock_once_opt(prices: List[float]) -> float:
    max_found = 0
    min_price = float("inf")
    for p in prices:
        max_found = max(max_found, p - min_price)
        min_price = min(p, min_price)
    return max_found


def buy_and_sell_stock_once_iter(prices: List[float]) -> float:
    max_found = 0
    l = 0
    while l < len(prices) - 1:
        if prices[l] > prices[l + 1]:
            l += 1
        else:
            r = l + 1
            while r < len(prices) - 1 and prices[r] < prices[r + 1]:
                r += 1

            max_found = max(max_found, max(prices[r:]) - prices[l])
            l = r
    return max_found


def buy_and_sell_stock_once_recursive(prices: List[float]) -> float:
    def helper(prices, idx):
        while idx < len(prices) - 1 and prices[idx] > prices[idx + 1]:
            idx += 1
        if idx >= len(prices) - 1:
            return 0
        return max(helper(prices, idx + 1), max(prices[idx:]) - prices[idx])

    return helper(prices, 0)


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "buy_and_sell_stock.py", "buy_and_sell_stock.tsv", buy_and_sell_stock_once
        )
    )
