class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Jul 21 cp in-class mock
        
        # by 城主思路
        # TC: O(nlgn), nlgn for sorting
        # SC: O(n)
        
        # corner cases
        if intervals is None or len(intervals) == 0:
            return []
        
        # practice-needed
        # sort by the start val i[0] of interval i
        intervals.sort(key = lambda i : i[0])
        res = []
        
        cur = intervals[0]
        
        # intervals[1:]: next starts from the second interval makes more sense
        for next in intervals[1:]: 
            # print("cur: ",cur)
            # print("next: ",next)
            if cur[1] >= next[0]: # cur.end >= next.start: overlapped
                cur[1] = max(cur[1], next[1]) 
                # without max() will fail [[1,4],[2,3]]
            else:
                res.append(cur) # insert a new interval
                cur = next 
            
        res.append(cur) # will miss the last interval without this line
            
        return res
        