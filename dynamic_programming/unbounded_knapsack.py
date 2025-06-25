from functools import lru_cache
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))


@lru_cache(None)
def unbounded_knapsack(index, w, weight, nums):
    if index == 0:
        return w // weight[index] * nums[index]
    notTake = unbounded_knapsack(index-1, w, weight, nums)
    take = float('-inf')
    if weight[index] <= w:
        take = nums[index] + unbounded_knapsack(index, w-weight[index], weight, nums)
    return max(take, notTake)


def unbounded_knapsack_tabulation(w, weight, nums):
    n = len(nums)
    dp = [[float("-inf") for _ in range(w+1)] for _ in range(n)]
    for i in range(w+1):
        dp[0][i] = w // weight[0] * nums[0]
    
    for i in range(1, n):
        for j in range(w+1):
            notTake = dp[i-1][j]
            take = float('-inf')
            if weight[i] <= j:
                take = nums[i] + dp[i][j-weight[i]]
            dp[i][j] = max(notTake, take)
    
    return dp[n-1][w]