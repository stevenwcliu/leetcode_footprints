class Solution:
    def intToRoman(self, num: int) -> str:
        # nc
        
        # order matters so use list of list instead of hm
        # iterate the list in reverse order
        
        # added the special rules for 4, 40, 90, 400, 900
        symbolList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], 
                      ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400], 
                      ["D", 500], ["CM", 900], ["M", 1000]]
        
        res = ""
        for sym, val in reversed(symbolList):
            if num // val:
                cnt = num // val # how many times we want to add this symbol to the res
                res += (sym * cnt)
                num = num % val # use the updated val in the next iteration
        print(res)
        return res