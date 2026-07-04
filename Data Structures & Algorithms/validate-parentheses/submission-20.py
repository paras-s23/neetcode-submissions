class Solution:
    def isValid(self, s: str) -> bool:
        closing = {"}" : "{", "]" : "[", ")" : "("}
        stack = []

        for p in s:
            if p in closing:
                if len(stack) == 0 or stack.pop() != closing[p]:
                    return False
            else:
                stack.append(p)
        return len(stack) == 0
