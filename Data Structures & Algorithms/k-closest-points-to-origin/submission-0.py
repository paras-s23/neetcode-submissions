import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k >= len(points):
            return points

        distances = []
        result = []

        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            distances.append((-distance, [x, y]))

        max_heap = distances[:k]
        heapq.heapify(max_heap)

        for value in distances[k:]:
            heapq.heappush(max_heap, value)
            heapq.heappop(max_heap)

        while max_heap:
            distance, point = heapq.heappop(max_heap)
            result.append(point)

        return result