from typing import List



class Solution:
    '''
    Pick no pick algorithm 
    '''
    def combinationSum(self, c: List[int], t: int) -> List[List[int]]:
        self.ans = []
        self.path = []
        self.n = len(c)
        def backtrack(i, sm, t):
            if i >= self.n:
                return
            if sm == t:
                self.ans.append(self.path[:])
                return
            if sm  > t:
                return
            self.path.append(c[i])
            backtrack(i, sm + c[i], t)
            self.path.pop()
            backtrack(i+1, sm, t)
        
        backtrack(0, 0, t)
        return self.ans
    

class Solution:
    def combinationSum2(self, arr: List[int], target: int) -> List[List[int]]:
        arr.sort()
        ans = []

        def solve(ds, i, sm):
            if sm == target:
                ans.append(ds.copy())
                return
            if sm > target or i >= len(arr):
                return
            for j in range(i, len(arr)):
                # Skip duplicates
                # Skip duplicate elements at same level to avoid duplicate combinations
                # Only skip if we're not at the first element of this recursion level (j > i)
                # and current element equals previous element
                if j > i and arr[j] == arr[j - 1]:
                    continue
                if arr[j] > target: break
                ds.append(arr[j])
                solve(ds, j + 1, sm + arr[j])
                ds.pop()

        solve([], 0, 0)
        return ans
        
            
                
        