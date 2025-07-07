from bisect import bisect_left
from typing import List

class Solution1:
    """
    Dynamic Programming solution for Longest Increasing Subsequence (LIS), with both
    top-down (memoized recursion) and bottom-up (tabulation) approaches.

    We want the length of the longest strictly increasing subsequence in the list `nums`.

    Top-down key idea:
      • Define solve(i, prev) as the length of the LIS starting at index i,
        given that the last included element is at index prev (or prev = -1 for none).
      • At each position i, we have two choices:
          1. Skip nums[i]: notTake = solve(i + 1, prev)
          2. Take nums[i] (only if prev == –1 or nums[prev] < nums[i]):
             take = 1 + solve(i + 1, i)
      • We memoize on (i, prev+1) to avoid recomputation.

    Bottom-up key idea:
      • Build a 2D table dp where dp[i][p] corresponds to solve(i, p-1) above.
      • Fill dp in reverse order of i, and for each prev index from i-1 down to -1.
      • The recurrence mirrors the two choices in the top-down approach.

    Time Complexity:
      • Top-down with memo: O(n²) in the worst case (n positions × n possible prev values)
      • Bottom-up: O(n²) for filling the table.
    Space Complexity:
      • O(n²) for the memo table or dp table.
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # Memoization map: keys are (i, prev+1) → LIS length from i given last at prev
        mp = {}

        def solve(i: int, prev: int = -1) -> int:
            # Base case: reached end of array
            if i == n:
                return 0
            # Check memo: use prev+1 to allow prev == -1
            if (i, prev + 1) in mp:
                return mp[i, prev + 1]

            # Option 1: skip current element
            not_take = solve(i + 1, prev)

            # Option 2: take current element if it makes an increasing sequence
            take = 0
            if prev == -1 or nums[prev] < nums[i]:
                take = 1 + solve(i + 1, i)

            # Memoize and return the best of the two choices
            mp[i, prev + 1] = max(take, not_take)
            return mp[i, prev + 1]

        # Compute via top-down recursion
        # return solve(0, -1)

        # Alternatively, bottom-up tabulation:
        # dp[i][p] = LIS length from index i when last taken index is p-1
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        # Fill table in reverse order of i
        for i in range(n - 1, -1, -1):
            # prev goes from i-1 down to -1
            for prev in range(i - 1, -2, -1):
                # Case 1: skip nums[i]
                length = dp[i + 1][prev + 1]
                # Case 2: take nums[i] if valid
                if prev == -1 or nums[prev] < nums[i]:
                    length = max(length, 1 + dp[i + 1][i + 1])
                dp[i][prev + 1] = length

        # The answer is dp[0][0]: starting at index 0 with no previous element
        return dp[0][0]


class Solution:
    """
    Optimized Dynamic Programming solution for Longest Increasing Subsequence (LIS)
    using O(n) extra space.

    We build an array dp where dp[i] is the length of the LIS ending exactly at index i.
    For each i, we look at all j < i:
      • If nums[i] > nums[j], we can extend the subsequence ending at j:
            dp[i] = max(dp[i], dp[j] + 1)

    Finally, the length of the overall LIS is max(dp).

    Initialization:
      - dp[i] = 1 for all i, since each element is itself a subsequence of length 1.

    Time Complexity: O(n²) due to the nested loops.
    Space Complexity: O(n) for the dp array.
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Edge case: empty list has LIS length 0
        if not nums:
            return 0

        n = len(nums)
        # dp[i] = length of LIS ending at index i
        dp = [1] * n

        # printing the LIS 
        hash = [0] * n
        maxi = 1;
        lastIndex = 0

        # Build dp iteratively
        for i in range(1, n):
            hash[i] = i
            for j in range(i):
                # If nums[i] can extend the sequence at j, update dp[i]
                if nums[i] > nums[j] and 1 + dp[j] > dp[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    hash[i] = j
            
            if dp[i] > maxi:

                maxi = max(maxi, dp[i])
                lastIndex = i

        # tracing longest increasing subsequence
        lis = [] 
        lis.append(nums[lastIndex])     
        while hash[lastIndex] != lastIndex:
            lastIndex = hash[lastIndex]
            lis.append(nums[lastIndex])
        
        print(lis[::-1])

        # The result is the maximum over all dp[i]
        return maxi
    
    def lengthOfLISBinarySearch(self, nums: List[int]) -> int:
        temp: List[int] = []
        temp.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] > temp[-1]:
                temp.append(nums[i])
            else:
                ind:int= bisect_left(temp, nums[i])
                temp[ind] = nums[i]
        
        return len(temp)


print(Solution().lengthOfLISBinarySearch([10,9,2,5,3,7,101,18]))