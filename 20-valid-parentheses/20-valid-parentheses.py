# nc updated
class Solution:
    def isValid(self, s: str) -> bool:
        # corner case: odd num chars
        
        if len(s) % 2 == 1:
            return False

        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
                
        