class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums) 
        curMin, curMax = 1, 1

        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            
            curMax = max(n * curMax, n * curMin)