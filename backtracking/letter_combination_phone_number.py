from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        '''
        Un-optimised code
        '''
        if digits == "":
            return []
        self.ans = []
        self.m = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        def backtrack(start, s):
            if len(s) == len(digits):
                print(s)
                self.ans.append(s)
            else:
                for i in range(start, len(digits)):
                    mLen = self.m[int(digits[i])]
                    for j in range(len(mLen)):
                        backtrack(i+1, s+mLen[j])
        backtrack(0, "")
        return self.ans
    

    def letterCombinations2(self, digits: str) -> List[str]:
        '''
        More optimised
        '''
        if not digits:
            return []

        self.ans = []
        self.m = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def backtrack(pos, path):
            if len(path) == len(digits):
                self.ans.append(path)
                return
            digit = int(digits[pos])
            for ch in self.m[digit]:
                backtrack(pos + 1, path + ch)

        backtrack(0, "")
        return self.ans