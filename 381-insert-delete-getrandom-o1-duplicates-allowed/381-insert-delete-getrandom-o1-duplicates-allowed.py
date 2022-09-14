from collections import defaultdict
import random

class RandomizedCollection:
    
    # ref: https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/discuss/822583/python-with-fix-of-solution-104ms-O(1)

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst = []
        self.d = defaultdict(set)  #{val: set of indexs}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.d[val].add(len(self.lst))
        self.lst.append(val)
        return len(self.d[val]) == 1
        
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.d or len(self.d[val]) == 0:
            return False
        idx, last = self.d[val].pop(), self.lst[-1] # cannot use pop for lst directly, can cause idx out of range issue later on if it's the last one or already empty list
        self.d[last].add(idx)
        self.lst[idx] = last
        self.d[last].remove(len(self.lst) -1)
        
        self.lst.pop()
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.lst)