# class Solution:
#     # cp 103 w3
#     # TC: O(N), [Single, non-nested iteration through the input string
#     # SC: O(N), stack
    
#     def calculate(self, s: str) -> int:
#         stack = [] # store sign and operand of previous expressions
#         operand = 0
#         res = 0 # For the on-going result
#         POSITIVE, NEGATIVE = 1, -1
#         sign = POSITIVE # 1 means positive, -1 means negative  

#         for c in s:
#             if c.isdigit():
#                 operand = (operand * 10) + int(c)
#                 print("operand: ", operand)

#             elif c == '+':
#                 res += sign * operand # add previous expression
#                 sign, operand = POSITIVE, 0

#             elif c == '-':
#                 res += sign * operand # still += !!
#                 sign, operand = NEGATIVE, 0

#             elif c == '(':
#                 stack.append(res)
#                 stack.append(sign)
#                 print("stack: ", stack)
#                 sign = POSITIVE
#                 res = 0

#             elif c == ')':
#                 res += sign * operand

#                 res *= stack.pop() # stack pop 1, sign
#                 res += stack.pop() # stack pop 2, operand

#                 # Reset the operand
#                 operand = 0

#         res += sign * operand
#         return res
    
# ref: https://fuxuemingzhu.cn/leetcode/224.html
from collections import deque
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, num, sign = 0, 0, 1
        stack = deque()
        for c in s:
						# 如果当前是数字，那么更新计算当前数字
            if c.isdigit(): 
                num = 10 * num + int(c)
						# 如果当前是操作符+或者-，那么需要更新计算当前计算的结果res，
						# 并把当前数字num设为0，sign设为正或负，重新开始
            elif c == "+" or c == "-":
                res = res + sign * num
                num = 0
                sign = 1 if c == "+" else -1
						# 如果当前是(，那么说明后面的小括号里的内容需要优先计算，
						# 所以要把res，sign进栈，更新res和sign为新的开始
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
						# 如果当前是)，那么说明当前括号里的内容已经计算完毕，
						# 所以要把之前的结果出栈，然后计算整个式子的结果
            elif c == ")":
                res = res + sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res = res + sign * num
        return res
        