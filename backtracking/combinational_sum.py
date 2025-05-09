from typing import List

class Solution:
    '''
    Solves the "Combination Sum" problem using the pick/not-pick recursion pattern.
    Elements can be reused unlimited times (unbounded).
    '''
    def combinationSum(self, c: List[int], t: int) -> List[List[int]]:
        self.ans = []   # Final result list
        self.path = []  # Current combination path (temporary)
        self.n = len(c) # Total number of candidates

        def backtrack(i, sm, t):
            # Base case: if index is out of bounds
            if i >= self.n:
                return
            
            # If the current sum equals the target, store a copy of the current path
            if sm == t:
                self.ans.append(self.path[:])  # [:] to copy current path
                return
            
            # If current sum exceeds target, no need to proceed
            if sm > t:
                return
            
            # ----------------------------
            # Choice 1: Pick current element again (same index)
            self.path.append(c[i])              # Choose the element
            backtrack(i, sm + c[i], t)          # Recurse with updated sum, same index
            self.path.pop()                     # Backtrack to try next possibility

            # ----------------------------
            # Choice 2: Skip current element and move to next
            backtrack(i + 1, sm, t)

        backtrack(0, 0, t)
        return self.ans


class Solution:
    '''
    Solves the "Combination Sum II" problem using backtracking.
    Each element can be picked only once. The list may contain duplicates,
    so we skip duplicates at the same recursion level.
    '''
    def combinationSum2(self, arr: List[int], target: int) -> List[List[int]]:
        arr.sort()  # Sort to group duplicates together and optimize early stopping
        ans = []

        def solve(ds, i, sm):
            # Base case: if sum equals target, add current combination to result
            if sm == target:
                ans.append(ds.copy())  # Store a deep copy of current path
                return

            # Base case: if sum exceeds target or we’re out of bounds
            if sm > target or i >= len(arr):
                return

            # Iterate through the remaining elements
            for j in range(i, len(arr)):
                # Skip duplicates at the same recursion level
                # (to avoid using the same element again in this level)
                if j > i and arr[j] == arr[j - 1]:
                    continue

                # Optimization: no need to proceed further if current number > target
                if arr[j] > target:
                    break

                # Choose arr[j]
                ds.append(arr[j])
                # Move to next index (each number can be picked only once)
                solve(ds, j + 1, sm + arr[j])
                # Backtrack to try next candidate
                ds.pop()

        solve([], 0, 0)
        return ans
