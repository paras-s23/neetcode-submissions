class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        if (k==1):
            return max(nums)
        
        k-=1
        nums.pop(nums.index(max(nums)))
        return self.findKthLargest(nums, k)