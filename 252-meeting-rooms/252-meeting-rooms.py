class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # Oct 8 review
        # nc
        # tc O(n)
        # sc O(1)
        intervals.sort(key = lambda i:i[0])
        
        for i in range(len(intervals) - 1):
            # compare ending time of the current meeting with the start time of the next one
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True