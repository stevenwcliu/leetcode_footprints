# cp 103 w6 warm-up
# ref: https://courses.codepath.org/courses/advanced_software_eng/pages/warmup_solutions/warmup_soln_6

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        for i in range(len(graph)):
            if i not in color:
                color[i] = 0
                if not self.dfs(i, graph, color):
                    return False
        return True

    def dfs(self, pos, graph, color):
        for i in graph[pos]:
            if i in color:
                if color[i] == color[pos]:
                    return False
            else:
                color[i] = 1 - color[pos]
                if not self.dfs(i, graph, color):
                    return False
        return True