class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        # dfs without memo 
        # tc O(??) ans: O(2^n), 2 possibilities at each step
        # sc O(n), depth of the recursion tree
#         def dfs(self, start_index):
#             if start_index == len(s): # we have constructed the entire target s
#                 return True

#             for word in words:
#                 if s[start_index:].startswith(word): # is this a valid path
#                     if dfs(self, start_index + len(word)):
#                           return True # any path leads to true is fine

#             return False

#         return dfs(self, 0)
    
        # dfs with memo 
        memo = {} # to cache the branches we have already seen
        # what to store in memo??
        
        def dfs(self, start_index):
            # base case
            if start_index == len(s): # we have constructed the entire target s
                return True
            
            if start_index in memo:
                return memo[start_index]
            
            ok = False

            for word in words:
                if s[start_index:].startswith(word): # is this a valid path
                    if dfs(self, start_index + len(word)):
                        # return True # any path leads to true is fine
                        ok = True
                        break
            # return False
            memo[start_index] = ok # ok == False
            return ok

        return dfs(self, 0)

#         # nc
#         # https://youtu.be/Sx9NNgInc3A
#         dp = [False] * (len(s) + 1)
#         dp[len(s)] = True

#         for i in range(len(s) - 1, -1, -1):
#             for w in wordDict:
#                 if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
#                     dp[i] = dp[i + len(w)]
#                 if dp[i]:
#                     break

#         return dp[0]

        # fxmz

        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # print(s)
        # print(wordDict)
        # dp = [False] * (len(s) + 1)
        # dp[0] = True
        # # print(dp)
        # for i in range(1, len(s) + 1):
        #     for k in range(i):
        #         if dp[k] and s[k:i] in wordDict:
        #             dp[i] = True
        #             # print(dp)
        # return dp[-1]