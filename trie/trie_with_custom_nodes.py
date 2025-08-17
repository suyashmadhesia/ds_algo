from typing import List    
        
class TrieNode:
    def __init__(self, val, end=False):
        self.val = val
        self.end = 0
        self.children = {}

    def __repr__(self):
        return f"{self.val}{f';n={self.end}' if self.end > 0 else ''}"


class Trie:
    def __init__(self):
        self.root = TrieNode("#")

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.end+= 1

    def _visualize(self, node, prefix, is_last):
        marker = "└── " if is_last else "├── "
        result = f"{prefix}{marker}{node}\n"
        children = list(node.children.values())
        for i, child in enumerate(children):
            is_last_child = i == len(children) - 1
            new_prefix = prefix + ("    " if is_last else "│   ")
            result += self._visualize(child, new_prefix, is_last_child)
        return result

    def visualize(self):
        print(self._visualize(self.root, "", True))

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.end > 0
    

    def searchWith(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
    

    def wildcardSearch(self, word):
        def dfs(i, node):
            curr  = node
            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    for n in curr.children:
                        if dfs(j+1, curr.children[n]): return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]

            return curr.end > 0
        
        return dfs(0, self.root)