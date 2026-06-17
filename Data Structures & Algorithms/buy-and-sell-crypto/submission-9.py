class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]

        for num in prices:
            maxProfit = max(maxProfit,num-minPrice)
            minPrice = min(minPrice, num)
        return maxProfit