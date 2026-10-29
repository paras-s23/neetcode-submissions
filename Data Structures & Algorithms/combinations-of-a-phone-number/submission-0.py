class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        result = []
        
        phone_map = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }

        def dfs(string, i):
            if len(string) >= len(digits):
                result.append(string)
                return
            for char in phone_map[digits[i]]:
                string+=char
                dfs(string, i+1)
                string = string[:-1]

        dfs("", 0)
        return result