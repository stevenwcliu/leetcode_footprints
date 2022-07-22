class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # corner cases
        if intervals is None or len(intervals) == 0:
            return []
        
        # practice-needed
        # sort by the start val i[0] of interval i
        intervals.sort(key = lambda i : i[0])
        res = [] # initialized with the first element to avoid an edge case??
        
        cur = intervals[0]
        
        for next in intervals:
            if cur[1] >= next[0]:
                cur[1] = max(cur[1], next[1])
            else:
                res.append(cur)
                cur = next
            
        res.append(cur)
            
        return res
        