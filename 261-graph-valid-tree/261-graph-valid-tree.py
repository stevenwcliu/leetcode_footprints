class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False
        g, q = {i:[] for i in range(n)}, [0]
        for u, v in edges:
            g[u].append(v), g[v].append(u)
        for x in q:
            q += g.pop(x, [])
        return not g
        