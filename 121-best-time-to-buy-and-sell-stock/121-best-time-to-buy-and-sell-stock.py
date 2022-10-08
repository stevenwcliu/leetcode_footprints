class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # nc
        # two-pointer
        # tc O(n)
        # sc O(1)
        
        l, r = 0, 1 # l = buy, r = sell
        maxP = 0 # 不熟：怎麼設無限值
        
        while r < len(prices):
            if prices[l] < prices[r]: # profitable
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                # 小心：不是 l += 1 
                # why: shift l all the way to r because we want l to be at the minimum
                l = r
            r += 1
        
        return maxP
            
            
            