# TC O(N^2)
# SC O(N)
# fuxuemingzhu 方法一：拓扑排序，BFS

from collections import defaultdict

class Solution(object):
    '''
    def canFinish(self, N, prerequisites):
        """
        :type N,: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = defaultdict(list) # courseDict
        indegrees = defaultdict(int)
        
        for u, v in prerequisites:
            graph[v].append(u) # u: next course, v: prev course
            indegrees[u] += 1
            
        print("graph: ", graph) # {0: [1]}
        print("indegrees: ", indegrees) # {1:1}
        
        # build graph - ref from nc
        # preMap = { i:[] for i in range(N)} 
        # for crs, pre in prerequisites:
        #     preMap[crs].append(pre)
        # print("preMap: ", preMap) # {0: [], 1: [0]}
        
        for i in range(N):
            zeroDegree = False
            for j in range(N):
                if indegrees[j] == 0:
                    zeroDegree = True
                    break
            if not zeroDegree: return False
            indegrees[j] = -1
            for node in graph[j]:
                indegrees[node] -= 1
        return True
    
    '''

    # 103 w7 warm-up
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ad_list = {i: set() for i in range(numCourses)}
        degrees = [0] * numCourses
        for prereq, course in prerequisites:
            ad_list[prereq].add(course)
            degrees[course] += 1
        
        eligibleCourses = []
        for course in range(numCourses):
            if degrees[course] == 0:
                eligibleCourses.append(course)
        
        i = 0
        while i < len(eligibleCourses):
            next_course = eligibleCourses[i]

            for course in ad_list[next_course]:
                degrees[course] -= 1
                if degrees[course] == 0:
                    eligibleCourses.append(course)
            
            i += 1
        
        return len(eligibleCourses) == numCourses
