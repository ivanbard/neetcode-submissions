class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices[i] is the price of coin on ith day
        # profit = sell price - buy price
        # maximize the profit, and return it

        min_price = prices[0]
        max_profit = 0

        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return max_profit