from typing import List


class Solution:
    '''
    Func to find all subsets of an array
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.temp = []
        self.ans = []
        self.n = len(nums)
        def sub(i):
            self.ans.append(self.temp[:])
            for j in range(i+1, self.n):
                self.temp.append(nums[j])
                sub(j)
                self.temp.pop()
        sub(-1)
        return self.ans
        


        