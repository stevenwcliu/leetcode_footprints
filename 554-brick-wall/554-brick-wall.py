class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        lines = {}
        for row in wall:
            sum = 0 
            for brick in row[:-1]:
                sum += brick
                lines[sum] = lines.get(sum,0) + 1
                # thisdict.get("model")
        if len(lines) < 1:
            return len(wall)
        else:
            return len(wall) - max(lines.values())