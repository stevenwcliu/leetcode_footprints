from random import randint
class RandomizedSet:

    def __init__(self):
        self.set = []
        
    def insert(self, val: int) -> bool:
        if val in self.set:
            return False
        else:
            self.set.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        if val not in self.set:
            return False
        else:
            self.set.remove(val) # supposed to pop the element
            return True
        
    def getRandom(self) -> int:
        # math.random func
        size = len(self.set)
        randomNum = randint(0, size - 1)
        # print("randomNum: ", randomNum)
        return self.set[randomNum]
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()