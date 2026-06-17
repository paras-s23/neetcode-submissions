class Solution:
    def isValid(self, s: str) -> bool:
        closing = {")" : "(", "]" : "[", "}":"{"}
        stack = []
        for c in s:
            if c in closing:
                if len(stack) == 0:
                    return False
                if stack.pop() != closing[c]:
                    return False
                continue
            stack.append(c)
        if len(stack) == 0:
            return True
        else:
            return False