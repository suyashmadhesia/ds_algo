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
    

class Solution2:
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
        
        return int(mini)


class Solution3:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        """
        Problem: Target Sum (Leetcode: https://leetcode.com/problems/target-sum/)

        Goal:
        Assign '+' and '-' signs to elements in 'nums' such that the resulting sum equals 'target'.
        Return the number of different expressions that evaluate to 'target'.

        Intuition:
        This is a variation of the subset sum problem and can be reduced to counting the number of subsets
        that sum up to a derived value using a mathematical transformation.

        Observation:
        Let us partition the array into two subsets: S1 (with '+' sign) and S2 (with '-' sign)
        Let:
            sum(S1) - sum(S2) = target      -- (i)
            sum(S1) + sum(S2) = totalSum    -- (ii), where totalSum = sum(nums)

        Adding (i) and (ii):
            2 * sum(S1) = target + totalSum
            => sum(S1) = (target + totalSum) / 2

        This means:
            We need to count the number of subsets whose sum is (target + totalSum) / 2

        Therefore, the problem is reduced to:
            Count the number of subsets of 'nums' whose sum is (target + totalSum) // 2

        Important Edge Cases:
        - If (target + totalSum) is odd, it's not possible to find an integer subset sum. Return 0.
        - If target > totalSum or target < -totalSum, it's also impossible. Return 0.

        Approach:
        1. Convert the problem to a subset sum count with sum = (target + totalSum) // 2.
        2. Use memoization (top-down DP) to count the number of ways to reach this subset sum.
        3. Special care for zero values: 
           When nums[0] == 0 and t == 0, there are two ways (include or exclude the zero).

        Time Complexity: O(N * s), where N is the number of elements and s is the target subset sum.
        Space Complexity: O(N * s) for memoization table.

        This approach works correctly even if the array contains zero or negative elements.
        """
        total = sum(nums)
        if (target + total) % 2 != 0 or target > total or target < -total:
            return 0
        
        s = (target + total) // 2
        n = len(nums)

        dp = [[-1 for _ in range(s + 1)] for _ in range(n)]

        def solve(i, t):
            if i == 0:
                if t == 0 and nums[0] == 0:
                    return 2
                if nums[0] == t or t == 0:
                    return 1
                return 0

            if dp[i][t] != -1:
                return dp[i][t]
            
            not_take = solve(i - 1, t)
            take = 0
            if nums[i] <= t:
                take = solve(i - 1, t - nums[i])

            dp[i][t] = take + not_take
            return dp[i][t]

        return solve(n - 1, s)