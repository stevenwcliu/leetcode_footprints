class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # ref: nc
        
        # brute force: tc O(2^n)
        # better: dfs + caching -> DP: tc O(n^2) 
        
        # tc: O(nlogn), for sorting
        # sc: O(nlogn), for sorting
        diffs = []
        
        for c1, c2 in costs:
            # diffs.append(c2 - c1, c1, c2) # type error
            diffs.append([c2 - c1, c1, c2])
            
        diffs.sort()
        
        res = 0
        
        for i in range(len(costs)):
            if i < len(costs) // 2: # get the first half
                res += diffs[i][2]
            else:
                res += diffs[i][1]
        
        return res
                       
                       
                       
        