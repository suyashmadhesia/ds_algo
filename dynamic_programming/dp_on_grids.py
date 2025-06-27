from functools import lru_cache
from math import inf
from collections import defaultdict


from collections import defaultdict
from typing import List, Union

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        🔹 Step 1: Brute Force Recursion
        Think recursively: From any cell (i, j), we can come either from:
        the top cell (i-1, j) — meaning we moved down to reach (i, j)
        the left cell (i, j-1) — meaning we moved right to reach (i, j)
        So, the number of paths to reach (i, j) is:


        🔹 Step 2: Identify Overlapping Subproblems
        In this recursive approach, we calculate the same subproblems again and again.
        Example:
        To compute solve(2, 2), we compute solve(1, 2) and solve(2, 1)
        But solve(1, 2) will again call solve(0, 2) and solve(1, 1)
        solve(1, 1) is now being called from both branches
        ⛔ Exponential time — O(2^(m+n))

        To fix this, we cache the results of subproblems so we don’t compute them more than once.
        Use a dictionary (like defaultdict) or a 2D list to store results of solve(i, j) once calculated.   
        """
        cache = defaultdict(int)

        def solve(i, j):
            # Base case: start position
            if i == 0 and j == 0:
                return 1
            # Out of bounds
            if i < 0 or j < 0:
                return 0
            # If already computed, return cached result
            if (i, j) in cache:
                return cache[i, j]
            # Otherwise, compute and cache
            cache[i, j] = solve(i-1, j) + solve(i, j-1)
            return cache[i, j]
        
        return solve(m-1, n-1)  # Start from bottom-right


class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Solve same like unique paths but we will take maximum from the path we will traversing
        """
        cache = {}
        def solve(i, j):
            if i == 0 and j == 0:
                return grid[i][j]
            if i < 0 or j < 0:
                return inf
            if (i, j) in cache:
                return cache[i,j]
            cache[i, j] = grid[i][j] + min(solve(i-1, j), solve(i, j - 1))
            return cache[i,j]

        return solve(len(grid)-1, len(grid[0])-1)
    

class Solution3:
    """
    It is easy to see:
    Instead of having two paths starting from 0,0 and then other path from N,N. 
    We can have two people starting from 0,0 and find two paths that collects maximum cherries.
    First  person finds the path to collect maximum cherries and mark those cherries collected then
    Second person finds another path to collect maximum cherries. 

    Though here is the case where local maximum is not global maximum. 
    So having cherry pick up by person1 and then person2 won't give the correct result. 
    This approach fails to find the best answer to this case. 

    Reference : https://leetcode.com/problems/cherry-pickup/solution/
    Approach #1: Greedy [Wrong Answer] 
    11100
    00101
    10100
    00100
    00111
    In above example we should be able to pick all cherries. I leave it up to you to figure out two paths that collect all cherries. 
    But, with our approach person1 will collect 9 cherries leaving once that is on the right(1,4) and on the left(2,0). 
    Then person2 won't be able to collect both cherries he can collect only right one or only left one. 

    Approach #2: 
    Now, we know that we want collectively maximum cherries.
    So, we have to do the traversal of both paths at the same time and select maximum global answer. 
    The potential problem of this approach is double counting (if we collect same cherry in 2 paths), but this can be easily avoided in code.
    If both are at the same cell we count cherry only once.
    Following code is backtracking brute force so it is TLE.
    Time Complexity is : 4^N*N. As we are calling cherryPickup 4 times recursively with problem size N*N.

    """
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)

        @lru_cache(None)
        def dp(r1, c1, r2) -> Union[int, float]:
            c2 = r1 + c1 - r2  # total steps k = r1 + c1 = r2 + c2

            # If out of bounds or on a thorn
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n or \
               grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float('-inf')

            # If both have reached bottom-right
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]

            # Pick cherries (avoid double counting if same cell)
            result = grid[r1][c1]
            if (r1, c1) != (r2, c2):
                result += grid[r2][c2]

            # Move to next states (4 possibilities)
            result += max(
                dp(r1 + 1, c1, r2 + 1),  # both go down
                dp(r1 + 1, c1, r2),      # p1 down, p2 right
                dp(r1, c1 + 1, r2 + 1),  # p1 right, p2 down
                dp(r1, c1 + 1, r2)       # both go right
            )

            return result

        result = dp(0, 0, 0)
        return int(max(0, result))  # If no valid path, return 0