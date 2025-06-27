from functools import lru_cache

class UnboundedKnapsack:
    """
    Unbounded Knapsack Problem

    You have:
      - an array `weight` of item weights,
      - an array `nums`   of item values (profits),
      - a knapsack capacity `W`.

    Unlike 0/1 Knapsack, here you can take each item **unlimited** times.

    Intuition (“pick, maybe pick again, or move on”):
      1. Number the items 0…n−1.
      2. At item i with remaining capacity `w`, ask:
           • “What if I skip item i?” → solve for items 0…i−1 with the same `w`.
           • “What if I take item i?” (if weight[i] ≤ w)
             → add nums[i], reduce capacity by weight[i], BUT stay at the same item i
               (because you could take it again).
      3. Take the max of those two choices.
      4. Base case: at index 0, fill the knapsack with as many copies of item 0 as fit:
           (w // weight[0]) * nums[0]
      5. Memoize (or tabulate) to reuse overlapping results.

    Both approaches run in O(n·W) time and use O(n·W) space.
    """

    def unboundedKnapsackRecursive(self, weight: list[int], nums: list[int], W: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(index: int, remainingW: int) -> int:
            # Base case: only item 0 is available → pack as many as you can:
            if index == 0:
                return (remainingW // weight[0]) * nums[0]

            # Option A: skip item `index`
            not_take = dfs(index - 1, remainingW)

            # Option B: take item `index` (if it fits)
            take = float('-inf')
            if weight[index] <= remainingW:
                # After taking, stay at same index (unlimited copies allowed)
                take = nums[index] + dfs(index, remainingW - weight[index])

            # Return the better of skipping vs taking
            return max(not_take, take)

        # Start from last item with full capacity
        return dfs(n - 1, W)


    def unboundedKnapsackDP(self, weight: list[int], nums: list[int], W: int) -> int:
        n = len(nums)
        # dp[i][w] = max value using items 0…i with capacity exactly w
        dp = [[0] * (W + 1) for _ in range(n)]

        # --- Initialize for item 0 ---
        # If you only have item 0, you fill the knapsack with as many copies as fit
        for w in range(W + 1):
            dp[0][w] = (w // weight[0]) * nums[0]

        # --- Fill table for items 1…n-1 ---
        for i in range(1, n):
            for w in range(W + 1):
                # Option A: skip item i
                not_take = dp[i - 1][w]

                # Option B: take item i (if it fits)
                take = float('-inf')
                if weight[i] <= w:
                    # when taking, we stay on row i to possibly take again
                    take = nums[i] + dp[i][w - weight[i]]

                # Best of the two choices
                dp[i][w] = max(not_take, take)

        # Answer: max value using all items with capacity W
        return dp[n - 1][W]
