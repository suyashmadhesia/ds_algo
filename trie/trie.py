class TrieNode:

    def __init__(self, val=None, childern=[]):
        self._val = val
        self.chidren = []




class Trie:
    
    def __init__(self):
        self._root = TrieNode()


    def insert(self, word: str) -> None:
        ...
            


    def search(self, word: str) -> bool:
        ...


    def startsWith(self, prefix: str) -> bool:
        ...

    



