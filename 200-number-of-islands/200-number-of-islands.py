# oc
# aug 9
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        cnt = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(grid, r, c): # 出界或者已访问过就停止
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            
            grid[r][c] = "0" # 访问过的做标记
            # 搜邻居
            dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in dir:
                dfs(grid, r + dr, c + dc)
                
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    cnt += 1
                    dfs(grid, r, c)
        return cnt
        