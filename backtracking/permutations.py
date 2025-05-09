from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)             # Number of elements
        self.perms = []                # Current permutation being built
        self.hs = [False] * self.n     # Visited flags for each index
        self.ans = []                  # Final result list

        def pem():
            # If the current permutation has all elements, store a copy
            if len(self.perms) == self.n:
                self.ans.append(self.perms.copy())
                return
        
            # Try each element in nums
            for j in range(0, self.n):
                if self.hs[j]: continue  # If already picked in current path, skip
                self.hs[j] = True        # Mark as used
                self.perms.append(nums[j])  # Add to current path
                pem()                       # Recurse
                self.hs[j] = False          # Backtrack
                self.perms.pop()            # Remove last added element
        
        pem()
        return self.ans


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start):
            # If we've placed all elements
            if start == len(nums):
                res.append(nums[:])  # Copy current arrangement
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]  # Swap current with i
                backtrack(start + 1)                         # Recurse with next index
                nums[start], nums[i] = nums[i], nums[start]  # Backtrack swap

        backtrack(0)
        return res
