# nc updated with comments from lc sol
# oct 5, 2022
# grind75
class Solution:
    def isValid(self, s: str) -> bool:
        # corner case: odd num chars
        # if len(s) % 2 == 1:
        #     return False

        mapping = {")": "(", "]": "[", "}": "{"} # use to check if the incoming close bracket matches with the existed open bracket in the stack 
        stack = [] # keep track of opening brackets

        for c in s:
            if c not in mapping:
                stack.append(c)
                continue
            if not stack or stack[-1] != mapping[c]:
                return False
            stack.pop() # the element at the top of the stack is an opening bracket of the same type, then we pop it off the stack and continue processing
            
        # In the end, if the stack is empty, then we have a valid expression.
        return not stack
                
        