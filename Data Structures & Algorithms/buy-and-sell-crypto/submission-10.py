class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minP = prices[0]

        for num in prices:
            maxProfit = max(maxProfit, num - minP)
            minP = min(minP, num)
        return maxProfit