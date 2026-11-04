class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        start, end = intervals[0][0], intervals[0][1]
        prevStart = start
        prevEnd = end

        for i in range(1, len(intervals)):
            if intervals[i][0] <= prevEnd:
                prevEnd = max(intervals[i][1],prevEnd)
                continue
            else:
                result.append([start, prevEnd])
                start = intervals[i][0]
                prevEnd = intervals[i][1]
        result.append([start, prevEnd])
        return result
