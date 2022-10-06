class Solution:

#     def add_to_stack(self, stack, char):
#         if not stack or stack[-1][0] != char: # empty stack or diff char than the top one
#             stack.append((char, 1)) # char, freq
#         else:
#             stack.append((char, stack[-1][1]+1))


#     def removeDuplicates(self, s: str, k: int) -> str:
#         stack = []
#         idx = 0
#         while idx < len(s):
#             # add similar characters to stack b4 crushing
#             while idx < len(s) and stack and s[idx] == stack[-1][0]:
#                 self.add_to_stack(stack, s[idx])
#                 idx += 1

#             # crush
#             # if stack and stack[-1][1] >= 3:
#             if stack and stack[-1][1] >= k:
#                 char = stack[-1][0]
#                 while stack and stack[-1][0] == char:
#                     print("hey")
#                     stack.pop()

#             # add next
#             if idx < len(s):
#                 self.add_to_stack(stack, s[idx])
#                 idx += 1

#         return "".join([item[0] for item in stack])

    # ref: lee215 
    # https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/discuss/392933/JavaC++Python-Two-Pointers-and-Stack-Solution
    # tc O(n)
    # sc O(n)
    def removeDuplicates(self, s, k):
        stack = [['#', 0]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * k for c, k in stack)