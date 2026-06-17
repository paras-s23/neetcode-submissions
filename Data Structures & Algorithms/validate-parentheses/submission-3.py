class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        
        for i in range(len(s)):
            if s[i] in closeToOpen.values():
                stack.append(s[i])
                continue
            
            if len(stack) == 0:
                return False
            rec = stack.pop()
            if closeToOpen[s[i]] == rec:
                continue
            else:
                return False
        if len(stack) != 0:
            return False
        return True