from collections import defaultdict


class Trie:

    def __init__(self):
        self._root = defaultdict(str)

    def insert(self, word: str) -> None:
        temp = self._root
        for char in word:
            if char not in temp:
                temp[char] = {}
            temp = temp[char]
        temp["#"] = True

    def search(self, word: str) -> bool:
        temp = self._root 
        for char in word:
            if char not in temp:
                return False
            temp = temp[char]
        return "#" in temp

    def startsWith(self, prefix: str) -> bool:
        temp = self._root 
        for char in prefix:
            if char not in temp:
                return False
            temp = temp[char]
        return True

    def searchWithDot(self, word: str) -> bool:
        def dfs(j, node):
            curr = node
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for n in curr:
                        if n == "#":
                            continue
                        if dfs(i+1, curr[n]):
                            return True
                    return False
                else:
                    if c not in curr:
                        return False
                    curr = curr[c]
            return '#' in curr
        return dfs(0, self._root)


t = Trie()
t.insert("bad")


print(t._root)
# print(t.startsWith("app"))
print(t.searchWithDot("b.."))

