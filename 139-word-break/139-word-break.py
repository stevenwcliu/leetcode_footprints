class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
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
        dp = [False] * (len(s) + 1)
        dp[0] = True
        # print(dp)
        for i in range(1, len(s) + 1):
            for k in range(i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True
                    # print(dp)
        return dp[-1]