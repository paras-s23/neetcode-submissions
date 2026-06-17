class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # BRUTE FORCE
        res = 0
        for l in range(len(heights)):
            for r in range(1+l, len(heights)):
                area = (r-l)*(min(heights[l], heights[r]))
                res = max(area, res)
        return res