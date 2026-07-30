class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            new_str = ""
            new_str+=(str(len(s)))
            new_str+=("#")
            new_str+=(s)
            res.append(new_str)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res

