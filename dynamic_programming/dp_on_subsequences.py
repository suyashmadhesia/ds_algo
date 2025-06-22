from collections import defaultdict
from functools import lru_cache
from typing import List
from math import inf


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Problem Link: https://leetcode.com/problems/partition-equal-subset-sum/description/

        Intuition:
        To solve this problem, we first observe that if the sum of all elements in the array is odd,
        it's impossible to partition it into two subsets with equal sum. Hence, we only proceed if the
        total sum is even.

        The problem then reduces to finding whether there exists a subset of the array whose sum is
        equal to half of the total sum (i.e., sum(nums) / 2). If such a subset exists, the remaining
        elements will naturally form the second subset with equal sum.

        We can solve this using either:
        1. Backtracking (top-down recursion with memoization): At each step, we decide whether to include
        the current number in the subset or not, and recursively check if the target can be achieved.
        2. Dynamic Programming (bottom-up): We use a 2D DP table where dp[i][j] indicates whether a
        subset of the first i elements can sum up to j. The solution lies in dp[n-1][target].

        Both approaches efficiently explore the subset combinations while avoiding redundant calculations.
        """

        n = len(nums)
        sm = sum(nums)
        if sm % 2 != 0:
            return False
        target = sm//2

        mp = defaultdict(bool)


        def solve(target, index):
            if target == 0:
                return True
            if index == 0: return nums[0] == target
            if (index, target) in mp: return mp[index, target]
            notTake = solve(target, index-1)
            take = False
            if target >= nums[index]: 
                take = solve(target-nums[index], index-1)
            mp[index, target] = take or notTake
            return mp[index, target]


        dp = [[False for _ in range(target+1)] for _ in range(n)] 
        for i in range(n):
            dp[i][0] = True
        if nums[0] <= target:
            dp[0][nums[0]] = True
        for i in range(1, n):
            for j in range(target+1):
                notTake = dp[i-1][j]
                take = False
                if nums[i] <= j:
                    take = dp[i-1][j-nums[i]]
                dp[i][j] = take or notTake
        
        return dp[n-1][target]
    

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """
        NOTE: not working solution if negatvie elements in array is present
        Problem: Minimum Subset Sum Difference

        Intuition:
        This problem is a variation of the classic "Partition Equal Subset Sum" problem.

        Goal:
        Split the given array into two subsets such that the absolute difference between their sums is minimized.

        Observation:
        Let the total sum of the array be 'totalSum'.
        We want to find two subsets S1 and S2 such that:
            |sum(S1) - sum(S2)| is minimized
        Since sum(S1) + sum(S2) = totalSum, the expression becomes:
            |totalSum - 2 * sum(S1)|

        Therefore, our task is reduced to finding a subset S1 such that:
            sum(S1) is as close as possible to totalSum // 2

        Approach:
        1. Use Dynamic Programming to find all achievable subset sums.
           We build a DP table dp[n][totalSum + 1], where:
               dp[i][j] = True if a subset of the first (i+1) elements can form sum 'j'
        2. After filling the DP table, check the last row for all possible subset sums <= totalSum // 2.
        3. For each valid subset sum 's', compute the absolute difference:
               |totalSum - 2 * s|
           Keep track of the minimum such difference.

        Why only check up to totalSum // 2?
        Any subset sum greater than totalSum // 2 will increase the difference.
        To minimize |S1 - S2|, we must make S1 and S2 as close as possible, so we only need to check sums up to totalSum // 2.

        Time Complexity: O(N * totalSum)
        Space Complexity: O(N * totalSum) (can be optimized to O(totalSum) using a 1D DP array)
        """

        n = len(nums)
        sm = sum(nums)
        target = sm
        dp = [[False for _ in range(target+1)] for _ in range(n)] 
        for i in range(n):
            dp[i][0] = True
        if nums[0] <= target:
            dp[0][nums[0]] = True
        for i in range(1, n):
            for j in range(target+1):
                notTake = dp[i-1][j]
                take = False
                if nums[i] <= j:
                    take = dp[i-1][j-nums[i]]
                dp[i][j] = take or notTake

        mini = inf
        for i in range(sm//2+1):
            if dp[n-1][i]:
                mini = min(mini, abs((sm - i) - i))
        
        return mini

