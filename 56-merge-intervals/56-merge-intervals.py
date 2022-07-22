class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # Jul 22 2nd review
        # TC: O(nlogn), sorting
        # SC: O(n), worst case: no overlapping
        
        # edge case
        if intervals is None or len(intervals) == 0:
            return []
        
        # sort by start
        intervals.sort(key = lambda i : i[0])
        
        res = []
        
        cur = intervals[0]
        
        for next in intervals[1:]:
            # overlap
            if cur[1] >= next[0]: # cur.end >= next.start
                cur[1] = max(cur[1], next[1]) # max() is important
            else:
                res.append(cur)
                cur = next
        
        res.append(cur) # add the last interval
        return res
