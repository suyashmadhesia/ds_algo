from typing import List
from bisect import bisect_left
from itertools import combinations

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        """
        Problem Link: https://leetcode.com/problems/minimum-difference-between-sums-of-two-subsets/description/

        Intuition:
        - The goal is to divide the array `nums` of size `2n` into two subarrays of size `n` each,
          such that the absolute difference between their sums is minimized.
        - A brute force solution would require generating all combinations of size `n` from the `2n` elements,
          which is computationally expensive (time complexity: C(2n, n) ≈ 10^9 for n=15).
        
        Optimal Strategy: Meet-in-the-Middle (MITM)
        ------------------------------------------------
        1. Split the original array into two halves (left and right), each of size `n`.
        2. For each half, generate all possible subset sums, **grouped by subset size**.
           This means, for `left`, you store all subset sums of size 0, 1, ..., n.
        3. For each possible split of subset sizes (k from left, n-k from right),
           try to find combinations where the total sum is closest to `total_sum / 2`.
        4. Use binary search to find the best match in the right half for each left half sum.

        Time Complexity:
        - O(2^n * n) for generating all subset sums and binary searching.
        - Works efficiently for `2n <= 30` (i.e., n ≤ 15).

        """

        n = len(nums) // 2
        left = nums[:n]     # First half
        right = nums[n:]    # Second half
        total_sum = sum(nums)

        def generate_subsets(arr):
            """
            Generate all possible subset sums grouped by subset size.
            For example:
            arr = [1, 2]
            Output:
            {
                0: [0],            # Sum of 0 elements
                1: [1, 2],         # Sums of all 1-element subsets
                2: [3]             # Sum of the 2-element subset
            }
            """
            subset_map = {}
            for k in range(len(arr)+1):
                # combinations(arr, k) gives all subsets of size k
                subset_sums = [sum(comb) for comb in combinations(arr, k)]
                subset_map[k] = sorted(subset_sums)  # Sort for binary search
            return subset_map

        # Generate subset sums grouped by size for both halves
        left_subsets = generate_subsets(left)
        right_subsets = generate_subsets(right)

        min_diff = float('inf')

        # Try all combinations: k elements from left, (n - k) from right
        for k in range(n + 1):
            left_list = left_subsets[k]
            right_list = right_subsets[n - k]

            for left_sum in left_list:
                # We want total_sum // 2 - left_sum ≈ right_sum
                # So that (left_sum + right_sum) is close to half the total sum
                target = total_sum // 2 - left_sum

                # Binary search to find the closest right_sum to target
                idx = bisect_left(right_list, target)

                # Check both idx and idx-1 to find the closest value
                for j in [idx, idx - 1]:
                    if 0 <= j < len(right_list):
                        right_sum = right_list[j]
                        combined = left_sum + right_sum
                        remaining = total_sum - combined
                        diff = abs(combined - remaining)
                        min_diff = min(min_diff, diff)

        return int(min_diff)
