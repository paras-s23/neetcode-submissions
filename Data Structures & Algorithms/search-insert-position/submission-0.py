class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if target > mid:
                if left == right:
                    return mid  + 1
                left = mid + 1
            elif target < mid:
                if left == right:
                    return mid  - 1
                right = mid -1
            else:
                return mid - 1