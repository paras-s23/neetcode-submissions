class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_dict = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in p_dict:
                if not stack:
                    return False
                if p_dict[c] != stack[-1]:
                    return False
                stack.pop(-1)
            else:
                stack.append(c)
        return True if not stack else False