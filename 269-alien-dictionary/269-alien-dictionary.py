# ref: grokking
# edge: a rule in the alien language
# at most, each pair of words can give us one rule
# tc: O(V + N)
# sc: O(V + N), storing all of the rules for each character in an adjacency list

'''
Failed case:
input: ["abc","ab"]
expected output: ''
'''

# in-degree: 接收哪些射线

from collections import deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 0:
            return ""
        
        # a. initialize the graph
        inDegree = {} # cnt of incoming edges
        graph = {} # adj list graph
        valid = True # !! 
        
        for word in words:
            for char in word:
                inDegree[char] = 0
                graph[char] = []
        # print("inDegree after initialization: ", inDegree)   
        # print("graph after initialization: ", graph)
        
        
        # b. Build the graph
        for i in range(0, len(words) - 1):
            # find ordering of chars from adj words
            w1, w2 = words[i], words[i + 1]
            # print("w1: ", w1)
            # print("w2: ", w2)
            if len(w1) > len(w2) and w1.startswith(w2):
                valid = False
            for j in range(0, min(len(w1), len(w2))):
                # why min(len(w1), len(w2)): 
                parent, child = w1[j], w2[j]
                # print("parent: ", parent)
                # print("child: ", child)
                if parent != child:
                    # if the two chars are diff, put child into parent's list
                    # print("hey")
                    graph[parent].append(child)
                    inDegree[child] += 1
                    break # only the first different character between the two words will help us find the order
        # print("inDegree after building: ", inDegree)   
        # print("graph after building: ", graph)
        
        if not valid:
            return ''
        
        # c. Find all sources
        sources = deque()
        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)
        
        # d. For each source, add it to the sortedOrder and subtract one from all its children's in-degrees
        
        sortedOrder = []
        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            for child in graph[vertex]: # get the node's children to decrement their in-degrees
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sources.append(child)
        
#         print("inDegre: ", inDegree)
#         print("sortedOrder: ", sortedOrder)
        if len(sortedOrder) != len(inDegree): # !! len(inDegree)
            return ''
        return ''.join(sortedOrder)
        
        