'''
Understanding:
- nodes: 

'''

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # visited = set() # rooms
        # stack = [rooms[0]] # keys
        
        stack = [0] # keys
        visited = set(stack)
        # print(stack)

        while stack:
            key = rooms[stack.pop()]
            # print("key: ", key)
            # for i in range(len(rooms)):
            # for i in rooms[key]:
            for i in key:
                if i not in visited:
                    visited.add(i)
                    # print("visited: ",visited)
                    stack.append(i)
                    # print("stack:", stack)
        return len(visited) == len(rooms)
    
    '''
    
    '''