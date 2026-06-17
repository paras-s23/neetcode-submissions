class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        track = {}

        for num in nums:
            if num in track:
                track[num] +=1
                continue
            track[num] = 1
        while k != 0:
            max_key = max(track, key=track.get)
            removed_value = track.pop(max_key)
            res.append(max_key)
            k-=1
        return res