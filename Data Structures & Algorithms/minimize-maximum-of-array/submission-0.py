class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        result = 0
        currSum = 0

        for i in range(len(nums)):
            currSum+=nums[i]
            com = (currSum + i) // (i + 1)
            result = max(result, com)
        return result

