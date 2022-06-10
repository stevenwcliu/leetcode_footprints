class Solution:
    # TC: O(m * n)
    # SC: O(m * n)??
    # cp 103 Jun 9 class exercise
    def leastBricks(self, wall: List[List[int]]) -> int:
        lines = {}
        for row in wall:
            sum = 0 
            for brick in row[:-1]:
                sum += brick # total number of collision at each col
                lines[sum] = lines.get(sum,0) + 1 
                
        if len(lines) < 1: # no collision at all?
            return len(wall)
        
        else:
            return len(wall) - max(lines.values())