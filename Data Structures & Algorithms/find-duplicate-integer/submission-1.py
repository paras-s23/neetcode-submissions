class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        temp = 0 

        for i in range(1, len(nums)):
            if nums[i] > temp:
                temp = nums[i]
                continue
            else:
                return nums[i]

        return -1