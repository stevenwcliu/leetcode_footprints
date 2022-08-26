

class Solution:
    def rob(self, nums: List[int]) -> int:
# nc
# aug 26
#         rob1, rob2 = 0, 0
        
#         for n in nums:
#             temp = max(n + rob1, rob2)
#             rob1 = rob2
#             rob2 = temp
#         return rob2

# fxmz
# dfs + memo
#         if not nums:
#             return 0
#         self.memo = dict()
#         return self.dfs(nums, len(nums) - 1)
    
#     # 在第 i 个房间之前（包括 i）能获取的最大收益
#     def dfs(self, nums, i):
#         if i in self.memo:
#             return self.memo[i]
#         res = 0
#         if i == 0:
#             res = nums[0]
#         elif i == 1:
#             res = max(nums[0], nums[1])
#         else:
#             res = max(self.dfs(nums, i - 1), self.dfs(nums, i - 2) + nums[i])
#         self.memo[i] = res
#         return res

# dp
        prev, cur = 0, 0
        for value in nums:
            prev, cur = cur, max(prev + value, cur)
        return cur

# oc logic in py
# ref: https://docs.google.com/presentation/d/1Vrjx-aYW6gIN99ccl5HLWyr1gj6lkSaVOQ-rdJdyuj4/edit#slide=id.gb3ea1f8943_0_19
# 状态：到第i天最大收益
# 选择：
# 今天不抢继承昨天
# 今天抢只能从前天过来

#         if len(nums) == 0:
#             return 0
        
#         dp = [None] * (len(nums) + 1)
#         dp[0] = 0
#         dp[1] = nums[0]
#         for i in range(2, len(nums) + 1):
#             dp[i] = max(nums[i - 1] + dp[i - 2], dp[i - 1])
#         return dp[len(nums)]