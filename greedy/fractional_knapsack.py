"""

✅ Q1. Basic Fractional Knapsack
Level: Easy
Problem:
Given N items with values and weights, and a knapsack capacity W, return the maximum value you can put into the knapsack. You can take fractions of items.

Constraints:
1 <= N <= 10^4
0 < weight[i] <= 10^5, 0 <= value[i] <= 10^5
0 < W <= 10^5


✅ Q2. Handle Zero-Value or Zero-Weight Items
Level: Medium
Problem:
Modify the previous implementation to correctly ignore items with weight = 0 and consider value = 0 items (as long as they don’t add weight). Return maximum value.

✅ Q3. Return Selected Items and Fractions
Level: Medium-Hard
Problem:
In addition to the maximum value, return the list of items taken, and the fraction of each taken.


✅ Q4. Multi-Constraint Fractional Knapsack
Level: Hard
Problem:
Each item has value, weight, and volume. The knapsack has a maximum weight and a maximum volume capacity. Find the maximum value by taking fractions of items. Use a greedy heuristic (e.g., value / (w + v)).

"""