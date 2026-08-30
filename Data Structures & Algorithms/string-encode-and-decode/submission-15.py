class Solution:

    def encode(self, strs: List[str]) -> str:

        res = []

        for s in strs:
            newStr = ''
            newStr+=str(len(s))
            newStr+="#"
            newStr+=s
            res.append(newStr)
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        og_list = []
        i=0
        while i<len(s):
            j = i
            while s[j] != "#":
                j+=1
            str_len = int(s[i:j])
            i = j + 1
            j = i + str_len
            og_list.append(s[i:j])
            i = j
        return og_list