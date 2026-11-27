from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        res = []
        last_seen = float('-inf')
        l = 0
        for i in range(len(s)):
            d[s[i]] = i
        for i in range(len(s)):
            last_seen = max(d[s[i]], last_seen)
            if i == last_seen:
                res.append(i-l+1)
                last_seen = float('-inf')
                l = i +1
        return res


        