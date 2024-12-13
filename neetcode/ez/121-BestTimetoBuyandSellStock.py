# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Problem:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            potential_profit = prices[i] - low
            if potential_profit > profit:
                profit = potential_profit
            # profit = max(profit, (prices[i] - low))
        if profit > 0:
            return profit
        else:
            return 0
