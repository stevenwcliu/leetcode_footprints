# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:
#         # Hint #3: Store coordinates of rotting oranges in a queue.
#         if not grid:
#             return -1
        
#         rows = len(grid)
#         cols = len(grid[0])
        
#         q = []
#         day = 0
        
#         for row in range(rows):
#             for col in range(cols):
#                 if grid[row][col] == 2: # rotten
#                     q.append((row, col, 0))
        
#         while q:
#             r, c, day = q.pop(0)
            
#             for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                 nr, nc = r + dr, c + dc
#                 if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
#                     q.append((nr, nc, day + 1))
#                     grid[nr][nc] == 2
        
#         # ??
#         for row in grid:
#             if 1 in row: # 1: fresh
#                 return -1
        
#         return day
        
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        queue = []
        day = 0
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2: # rotten
                    queue.append((row, col, 0))
                    
        while queue:
            r, c, day = queue.pop(0)
            
            for nr, nc in [r+1, c], [r-1, c], [r, c+1], [r, c-1]:
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1: # 1: fresh
                    queue.append((nr, nc, day + 1))
                    grid[nr][nc] = 2
        # without: faile [[2,1,1],[0,1,1],[1,0,1]]            
        for row in grid:
            if 1 in row:
                return -1
        
            
        return day