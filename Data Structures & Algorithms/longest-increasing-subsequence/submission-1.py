class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LTS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LTS[i] = max(LTS[i], 1 + LTS[j])
        
        return max(LTS)