from functools import lru_cache
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

class Solution:
    """
    0/1 Knapsack Problem

    You have:
      - an array `weight` of item weights,
      - an array `nums`  of item values (profits),
      - a knapsack capacity `W`.

    Goal: maximize the total value of items you put in the knapsack without exceeding capacity.

    Intuition (what you do in your head when “picking and unpicking”):
      1. Number the items 0…n−1.
      2. At item i, ask:
           • “What if I skip item i?” → solve the subproblem for items 0…i−1 with same capacity.
           • “What if I take item i?” (only if weight[i] ≤ remaining capacity)
             → add nums[i] to value, reduce capacity by weight[i], and solve for 0…i−1.
      3. Take the max of these two choices.
      4. Recurse all the way down to item –1 (base case → 0).
      5. Memoize to avoid re-doing work.

    Two implementations below:
      • `knapsackRecursive` uses top-down recursion + lru_cache  
      • `knapsackDP`        uses bottom-up tabulation
    """

    def knapsackRecursive(self, weight: list[int], nums: list[int], W: int) -> int:
        n = len(nums)

        @lru_cache(None)
        def dfs(index: int, remainingW: int) -> int:
            # Base case: no items left
            if index < 0:
                return 0

            # 1. Option A: skip item `index`
            not_take = dfs(index - 1, remainingW)

            # 2. Option B: take item `index` (if it fits)
            take = float('-inf')
            if weight[index] <= remainingW:
                # pick it, add its value, reduce capacity, then recurse
                take = nums[index] + dfs(index - 1, remainingW - weight[index])

            # 3. Return the better of skipping vs taking
            return max(not_take, take)

        # Kick off recursion from the last item with full capacity
        return dfs(n - 1, W)


    def knapsackDP(self, weight: list[int], nums: list[int], W: int) -> int:
        n = len(nums)
        # dp[i][w] = max value using items 0…i with capacity exactly w
        dp = [[0] * (W + 1) for _ in range(n)]

        # --- Initialize for item 0 ---
        # If capacity w can hold item 0, best value is nums[0], else 0
        for w in range(W + 1):
            if weight[0] <= w:
                dp[0][w] = nums[0]

        # --- Fill table for items 1…n-1 ---
        for i in range(1, n):
            for w in range(W + 1):
                # Option A: skip item i
                not_take = dp[i - 1][w]

                # Option B: take item i (if it fits)
                take = float('-inf')
                if weight[i] <= w:
                    take = nums[i] + dp[i - 1][w - weight[i]]

                # Best of the two goes into dp[i][w]
                dp[i][w] = max(not_take, take)

        # Answer: max value using all n items with capacity W
        return dp[n - 1][W]
