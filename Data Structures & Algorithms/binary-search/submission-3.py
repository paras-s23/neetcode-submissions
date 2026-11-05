class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left<=right:
            mid = (left+right)//2

            if target < nums[mid]:
                right = mid - 1 
            elif traget > nums_mid:
                left = mid +1
            else:
                return mid
        
        return -1