class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        freq = {}
        i = 0

        for char in p:
            freq[char] = freq.get(char, 0) + 1

        while i < len(s):
            j = i
            while j < len(s) and j < len(p) and s[j] in freq:
                j += 1

            if j == len(p):
                result.append(i)
                i = i + 1
                continue

            i = j + 1

        return result