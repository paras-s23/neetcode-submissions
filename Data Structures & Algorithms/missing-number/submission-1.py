class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_number = max(nums)
        for i in range(max_number):
            if i not in nums:
                return i
        return max_number + 1