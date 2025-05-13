"""

✅ Q1. Minimum Cost of Merging Files
Level: Easy
Problem:
You are given an array files where files[i] is the size of the i-th file. You can merge two files at a time. The cost of merging is the sum of their sizes. Find the minimum total cost to merge all files into one.

Constraints:
2 <= len(files) <= 10^4
1 <= files[i] <= 10^5



✅ Q2. Return Merge Sequence (Tree Representation)
Level: Medium
Problem:
Return a list of merges performed as pairs of file sizes. Each merge should be represented as a tuple (size1, size2) in the order they occurred.

Output Example:
Input: [2, 3, 4] → Output: [(2, 3), (5, 4)]
Explanation: Merge 2+3 → 5, then 5+4 → 9.


✅ Q3. k-way Merge Pattern
Level: Medium-Hard
Problem:
You are allowed to merge up to k files at a time instead of just 2. Each merge cost is the sum of the sizes of the merged files. Find the minimum total cost to merge all files into one.

Constraints:
2 <= k <= 10
len(files) >= k

✅ Q4. Non-linear Merge Cost
Level: Hard
Problem:
You are given files[i] and a cost function: merging files of sizes a and b costs (a + b)^2. Design an approximate greedy algorithm to minimize total cost.

Note: Greedy isn't always optimal here. Return total cost using a reasonable heuristic (e.g., smallest size first).


"""