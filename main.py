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


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict: trie.insert(word)
        n = len(s)
        def valid(i):
            if i == n:
                return True
            curr = trie.root
            for j in range(i, n):
                char=s[j]
                if char not in curr.children:
                    break
                curr = curr.children[char]
                if curr.end > 0:
                    if valid(j+1):
                        return True
            
            return False

        return valid(0)
    

# s = Solution().wordBreak("catsanddogs", ["cats","dog","sand","and","cat"])
# print(s) 


def solution(prices: List[int], algo: List[int], k: int) -> int:
    n = len(prices)
    # base revenue
    base = 0
    for p, a in zip(prices, algo):
        base += p if a == 1 else -p

    if k == 0 or n == 0:
        return base

    # sliding-window max of gains
    gain = [0]*n
    for i, (p, a) in enumerate(zip(prices, algo)):
        if a == 0:
            gain[i] = 2 * p

    window = sum(gain[:k])
    best = window
    for i in range(k, n):
        window += gain[i] - gain[i - k]
        if window > best:
            best = window

    return base + best


print(solution([2, 4, 1, 5, 2, 6, 7], [0, 1, 0, 0, 1, 0, 0], 4))