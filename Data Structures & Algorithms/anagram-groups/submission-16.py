from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for string in strs:
            freq = [0] * 26
            for i in range(len(string)):
                freq[ord(string[i]) - ord('a')] += 1
            
            d[tuple(freq)].append(string)
            
        return list(d.values())