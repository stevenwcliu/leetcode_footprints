class Solution:
    def knightDialer(self, N):
        # fxmz: https://fuxuemingzhu.cn/leetcode/935.html#%E7%A9%BA%E9%97%B4%E6%8D%A2%E6%97%B6%E9%97%B4-%E5%88%A9%E7%94%A8%E5%AF%B9%E7%A7%B0%E6%80%A7
        """
        :type N: int
        :rtype: int
        """
        # if N == 1: return 10
        # x1 = x2 = x3 = x4 = x5 = x6 = x7 = x8 = x9 = x0 = 1
        # MOD = 10 ** 9 + 7
        # for i in range(N - 1):
        #     x1, x2, x3, x4, x5, x6, x7, x8, x9, x0 = (x6 + x8) % MOD,\
        #         (x7 + x9) % MOD, (x4 + x8) % MOD, (x3 + x9 + x0) % MOD, 0, (x1 + x7 + x0) % MOD,\
        #         (x2 + x6) % MOD, (x1 + x3) % MOD, (x2 + x4) % MOD, (x4 + x6) % MOD
        # return (x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 + x9 + x0) % MOD
        
        # from Joey 
        dct = {1:[6, 8], 2:[7, 9], 3:[4, 8], 4:[0, 3, 9], 5:[], 6:[0, 1, 7], 7:[2, 6], 8:[1, 3], 9:[2, 4], 0:[4, 6]}
        
        moves = [1] * 10
        for _ in range(N - 1):  # exclude itself when move
            next_moves = [0] * 10    # nxt[6] = 1 nxt[8] = 1
            for curr_step in range(10):
                for next_step in dct[curr_step]:
                    next_moves[next_step] += moves[curr_step]

            moves = next_moves
        
        return sum(moves) % (10 ** 9 + 7)
