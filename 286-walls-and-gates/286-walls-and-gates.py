# ref: https://leetcode.com/problems/walls-and-gates/discuss/794419/Python-3-BFS

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return
        
        q = []
        
        m, n = len(rooms), len(rooms[0])
        
        for r in range(m):
            for c in range(n):
                if not rooms[r][c]: # ???
                    q.append((r,c))
        
        dis = 1
        while q:
            tmp_q = []
            while q:
                r, c = q.pop()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and rooms[nr][nc] == 2147483647:
                        rooms[nr][nc] = dis
                        tmp_q.append((nr, nc))
            
            q = tmp_q
            dis += 1