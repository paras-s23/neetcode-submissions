class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []
        freq = {}

        for char in p:
            freq[char] = freq.get(char, 0) + 1

        i = 0

        while i <= len(s) - len(p):
            j = i
            freq1 = {}

            while j - i < len(p):
                freq1[s[j]] = freq1.get(s[j], 0) + 1
                j += 1

            if freq1 == freq:
                result.append(i)

            i += 1

        return result