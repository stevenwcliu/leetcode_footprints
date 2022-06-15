# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # 大神模版
        # p, q = 0, n - 1 -> can't pass 1,1 
        p, q = 1, n
        while p <= q:
            mid = p + ( q - p ) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res < 0:
                q = mid - 1
            else:
                p = mid + 1
                
        return -1
        