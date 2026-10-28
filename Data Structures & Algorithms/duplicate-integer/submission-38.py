class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dd = set()

        for val in nums:
            if val in dd:
                return True
            dd.add(val)
        return False
        