class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        nums = sorted(nums)

        for i in range(len(nums)-1, -1,-1):
            result = nums[i]
            k-=1
            if k == 0:
                return result
        return -1