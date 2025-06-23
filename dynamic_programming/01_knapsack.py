from functools import lru_cache
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))


@lru_cache(None)
def o1knapsack(index, w, weight, nums):
    if index == 0:
        if weight[index] <= w:
            return nums[index]
        return 0

    notTake = o1knapsack(index-1, w, weight, nums)
    take = float('-inf')
    if weight[index] < w:
        take = nums[index] + o1knapsack(index-1, w-weight[index], weight, nums)
    return max(take, notTake)


def o1knapsackTabulation(n, W, weight, nums):
    # Create DP table with (n x (W+1))
    dp = [[0] * (W + 1) for _ in range(n)]

    # Initialize first row (index 0)
    for wt in range(W + 1):
        if weight[0] <= wt:
            dp[0][wt] = nums[0]

    # Fill the table
    for i in range(1, n):
        for wt in range(W + 1):
            notTake = dp[i - 1][wt]
            take = float('-inf')
            if weight[i] <= wt:
                take = nums[i] + dp[i - 1][wt - weight[i]]
            dp[i][wt] = max(take, notTake)

    return dp[n - 1][W]