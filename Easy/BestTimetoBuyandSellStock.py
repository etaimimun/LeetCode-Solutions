class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        currentHigh = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                currentHigh = max(currentHigh, profit)
            else:
                l = r
            r += 1
        return currentHigh
        