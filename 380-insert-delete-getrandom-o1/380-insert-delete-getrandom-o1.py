# # import random
# from collections import defaultdict

# class RandomizedSet:

#     '''
#     areas of improvements
#     - import defaultdict
#     - naming of vars
    
    
#     '''
#     def __init__(self):
#         # self.map = defaultdict()
#         # self.dict = defaultdict() 
#         self.dict = {}
#         # self.arr = []
#         self.list = []
        
#     def insert(self, val: int) -> bool: # O(1)
#         if val not in self.dict:
#             self.dict.append[val] = 0
#             return True
#         self.map[val] = len(self.arr)
#         self.arr.append(val)
#         return False
        
#     def remove(self, val: int) -> bool: # O(1)
#         if val in self.map.item():
#             temp = self.arr[-1]
#             self.map[val] = temp
#             self.arr[-1] = val 
#             self.arr.pop()
#             self.map.remove(val)
#             return True
#         else:
#             return False 
    # def getRandom(self) -> int: # O(1)
    #     random.choice(self.arr)
class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []
    
    def insert(self, val:int) -> bool:
        if val in self.dict:
            return False
        self.dict[val] = len(self.list) # val:index
        self.list.append(val)
        return True
    
    def remove(self, val:int) -> bool:
        if val in self.dict:
            last_element, index = self.list[-1], self.dict[val]
            # swap the last element in list with the element we want to remove
            # update the index of the last element in dict to be the original index of
            # the element to be removed
            self.list[index], self.dict[last_element] = last_element, index
            self.list.pop() # delete the last element from list
            del self.dict[val] # delete the corresponding key from dict
            return True
        return False
    
    def getRandom(self) -> int:
        # !!!
        # choice() returns a randomly selected element from the specified sequence
        if self.list:
            return choice(self.list)
        else:
            return False

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()