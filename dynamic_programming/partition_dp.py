# partition DP
from functools import lru_cache
from typing import List
"""
Question: Matrix chain multiplication;
Minimum number of steps require to mutliply matrixes


1. Start with entire block of array (i, j)
2. Try all possibility
3. Return Best two partitions

e.g arr = [10, 20, 30, 40, 50]
                A   B   c   D
                i           j

k = i-> j-1
why
f(1, k) f(k+1, j)

how this from
e.g arr = [10, 20, 30, 40, 50]
                A   B   c   D
                i   k       j
so partition is 
    A       B             C      D
10 * 20 20 * 30. ----- 30* 40 40 * 50
    \\                           /
    10*30                   30*50
        \\                   //
                10 * 30 * 50
                i-1. k.   j
"""
arr = [10, 20, 30, 40, 50]


@lru_cache(None)
def mcm(i, j):
    if i == j:
        return 0
    mini = 1e9
    for k in range(i, j):
        steps = arr[i-1] * arr[k] * arr[j] \
        + mcm(i, k) \
        + mcm(k+1, j)
        mini = min(mini, steps)
    return mini


def mcmTabulation(i, j):
    N = len(arr)
    dp = [[0] * N] * N
    for i in range(N):
        dp[i][i] = 0
    for i in range(N-1, 0, -1):
        for j in range(i+1, N):
            mini = 1e9
            for k in range(i, j):
                # same as recurrence relation from the mcm using recursion
                pass



class MatrixChainMultiplication:
    """
    Dynamic Programming solution for the Matrix Chain Multiplication (MCM) problem,
    featuring both a top-down (memoized recursion) and a bottom-up (tabulation) approach.

    Problem:
      Given a sequence of matrix dimensions dims of length n,
      there are (n−1) matrices where the i-th matrix has dimensions
      dims[i−1] × dims[i]. We wish to parenthesize the product
        M1 × M2 × … × M(n−1)
      so as to minimize the total number of scalar multiplications.

    Top‐down (memoized recursion) key idea:
      • Define solve(i, j) as the minimum cost to multiply the subchain of matrices
        from index i to j (inclusive), where i and j run from 1 to n−1.
      • Base case: solve(i, i) = 0, since a single matrix needs no multiplication.
      • For i < j, try every possible split k between i and j:
           cost = solve(i, k) + solve(k+1, j) + dims[i−1] * dims[k] * dims[j]
        and take the minimum over k.
      • Cache results of solve(i, j) to avoid recomputation.

    Bottom‐up (tabulation) key idea:
      • Build a 2D table dp of size n×n, where dp[i][j] stores the minimum cost
        for multiplying matrices i through j.
      • Initialize dp[i][i] = 0 for all i.
      • Fill dp by increasing chain length (L = 2 … n−1):
          for each start i = 1 … n−L:
            let j = i+L−1
            dp[i][j] = min over k in [i, j−1] of
              (dims[i−1]*dims[k]*dims[j] + dp[i][k] + dp[k+1][j])

    Time Complexity:
      • Top‐down with memoization: O(n³) in the worst case
      • Bottom‐up tabulation: O(n³) due to three nested loops (length, i, k)

    Space Complexity:
      • O(n²) for the dp table or memo cache.
    """
    def __init__(self, dims: List[int]):
        """
        :param dims: List of matrix dimensions of length n;
                     there are (n−1) matrices of dimensions
                     dims[i−1] × dims[i] for i = 1 … n−1.
        """
        self.dims = dims
        self.n = len(dims)

    def min_cost_top_down(self):
        """
        Computes the minimum multiplication cost using a top-down DP approach.
        """
        @lru_cache(None)
        def solve(i: int, j: int):
            # Base case: single matrix, no cost
            if i == j:
                return 0

            min_ops = float('inf')
            # Try all possible splits between i and j
            for k in range(i, j):
                # Cost = cost to multiply left subchain + right subchain
                #      + cost to multiply resulting two matrices
                cost_left  = solve(i, k)
                cost_right = solve(k + 1, j)
                cost_split = self.dims[i - 1] * self.dims[k] * self.dims[j]
                total_cost = cost_left + cost_right + cost_split

                # Keep track of minimum over all k
                if total_cost < min_ops:
                    min_ops = total_cost

            return min_ops

        # Solve for the full chain (matrices 1 through n−1)
        return solve(1, self.n - 1)

    def min_cost_bottom_up(self):
        """
        Computes the minimum multiplication cost using bottom-up tabulation.
        """
        # dp[i][j] = min cost to multiply matrices i through j
        # We only use indices 1…n−1 for actual matrices.
        dp = [[0] * self.n for _ in range(self.n)]

        # Chains of length L = 2 .. (n−1)
        for L in range(2, self.n):
            # i = start index of chain
            for i in range(1, self.n - L + 1):
                j = i + L - 1
                dp[i][j] = float('inf') # type: ignore

                # Try splitting at k
                for k in range(i, j):
                    # Cost to multiply (i..k) and (k+1..j), then combine
                    cost = (
                        dp[i][k]                    # cost of left subchain
                        + dp[k + 1][j]              # cost of right subchain
                        + self.dims[i - 1]           # rows of leftmost
                          * self.dims[k]             # columns of left / rows of right
                          * self.dims[j]             # columns of rightmost
                    )
                    if cost < dp[i][j]:
                        dp[i][j] = cost

        # Answer is cost to multiply full chain 1..(n−1)
        return dp[1][self.n - 1]


# Example usage:
if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    solver = MatrixChainMultiplication(arr)

    print("Top-down MCM cost:", solver.min_cost_top_down())      # → 38000
    print("Bottom-up MCM cost:", solver.min_cost_bottom_up())    # → 38000
