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


t = Trie()
t.insert("apple")
t.insert("apps")
t.insert("apk")

print(t._root)
print(t.startsWith("app"))
print(t.search("app"))
