# Aug 23 based on grokking
# https://www.educative.io/courses/grokking-the-coding-interview/m25rBmwLV00

# TC: O(V + E), in step d, each vertex will become a source only once and each edge will be accessed and removed once.

# SC: O(V + E), since we are storing all of the edges for each vertex in an adjacency list.
from collections import deque
class Solution:
    def findOrder(self, vertices: int, edges: List[List[int]]) -> bool:
        # numCources: vertices
        # prerequisites: edges
        
        sortedOrder = []
        # corner case check
        if vertices <= 0:
            return sortedOrder
        
        # a. initialize the graph
        graph = {i: [] for i in range(vertices)} # adj list graph
        inDegree = {i: 0 for i in range(vertices)} # cnt of incoming degrees
        
        # b. build the graph
        for edge in edges:
            # parent, child = edge[0], edge[1] # template
            parent, child = edge[1], edge[0] # talored based on input
            graph[parent].append(child) # put child into its parent's list
            inDegree[child] += 1
        
        # c. Find all sources(vertices with 0 indegree)
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        # d. For each source, add it to the sortedOrder and subtract one from all its' children's indegrees
        # if a child's in-degree becomes 0, add it to the sources queue
        # TC: O(V + E), each vertex will become a source only once and each edge will be accessed and removed once.
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            # get the node's children to decrement their in-degrees
            for child in graph[vertex]: # review
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
        if len(sortedOrder) != vertices:
            return []
        else:
            return sortedOrder
                
        