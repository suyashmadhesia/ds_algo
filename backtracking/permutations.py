from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        self.perms = []
        self.hs = [False] * self.n # create a map if the index is current index in the loop it means it is already picked so we need to skip it
        self.ans = []
        

        def pem():
            if len(self.perms) == self.n:
                self.ans.append(self.perms.copy())
                return
        
            for j in range(0, self.n):
                if self.hs[j]: continue
                self.hs[j] = True
                self.perms.append(nums[j])
                pem()
                self.hs[j] = False
                self.perms.pop()
        
        pem()
        return self.ans
        