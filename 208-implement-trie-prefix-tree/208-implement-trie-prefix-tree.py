# nc
# hand-typed

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False

class Trie:

    def __init__(self):
        '''
        initialize the data structure
        '''
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        '''
        insert a word into the trie
        '''
        curr = self.root
        for c in word:
            i = ord(c) - ord('a')
            if curr.children[i] == None:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.end = True

    def search(self, word: str) -> bool:
        '''
        returns if the word is in the trie
        '''
        curr = self.root
        for c in word:
            # i = ord('c') - ord('a')
            i = ord(c) - ord('a')
            if curr.children[i] == None:
                return False
            curr = curr.children[i] # missing
        return curr.end # !! reason of not just return True: ??

    def startsWith(self, prefix: str) -> bool:
        '''
        returns if there is any word in the trie starts with the given prefix
        '''
        
        curr = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if curr.children[i] == None:
                return False
            curr = curr.children[i]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)