class Solution:
    def isValid(self, s: str) -> bool:
        closing = {"]" : "[", "}" : "{", ")" : "("}
        stack = []

        for p in s:
            if p in closing:
                if len(stack) == 0 or closing[p] != stack.pop():
                    return False
            else:
                stack.append(p)
        return len(stack) == 0