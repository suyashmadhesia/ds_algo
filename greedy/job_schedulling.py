"""

✅ Q1. Maximize Profit from Job Scheduling
Level: Easy
Problem:
You are given N jobs, each with a deadline and a profit. Only one job can be scheduled at a time. Return the maximum total profit possible by scheduling the jobs within their deadlines.

# Test Case 1
jobs = [(2, 50), (1, 10), (2, 20), (1, 30)]
# Explanation: Schedule (2, 50) and (1, 30) => total profit = 80
Expected Output: 80

# Test Case 2
jobs = [(1, 100), (2, 19), (2, 27), (1, 25), (3, 15)]
# Expected: Schedule (1, 100), (2, 27), (3, 15) => total = 142
Expected Output: 142

# Test Case 3 - Edge case
jobs = []
Expected Output: 0
-----------------------------------------------------------------------------------------------

✅ Q2. Job Scheduling with Job Count
Level: Medium
Problem:
Return the number of jobs scheduled and the total profit.

# Test Case 1
jobs = [(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)]
# Selected jobs: (1, 100), (2, 27), (3, 15)
Expected Output: (3, 142)

# Test Case 2
jobs = [(1, 20), (1, 10), (1, 40)]
# Pick the highest profit with deadline 1
Expected Output: (1, 40)
-----------------------------------------------------------------------------------------------



✅ Q3. Job Scheduling with k Parallel Machines
Level: Medium-Hard
Problem:
You are given k machines that can work simultaneously. Return the maximum total profit by scheduling jobs optimally.

# Test Case 1
jobs = [(1, 20), (2, 60), (2, 40), (3, 30), (3, 10)]
k = 2
# Machines can do more in parallel — schedule (2,60)+(2,40)+(3,30)+(1,20) = 150
Expected Output: 150

# Test Case 2
jobs = [(1, 20), (1, 30), (1, 10)]
k = 2
# Max two machines, best two jobs with deadline 1
Expected Output: 50
-----------------------------------------------------------------------------------------------

✅ Q4. Job Scheduling with Duration
Level: Hard
Problem:
Each job has a start time, end time, and profit. Find the max profit with non-overlapping jobs.

# Test Case 1
jobs = [(1, 3, 50), (3, 5, 20), (6, 19, 100), (2, 100, 200)]
# Best is (2,100,200)
Expected Output: 200

# Test Case 2
jobs = [(1, 2, 50), (3, 5, 20), (6, 19, 100), (2, 100, 200), (101, 120, 150)]
# (2,100,200) + (101,120,150)
Expected Output: 350

# Test Case 3
jobs = [(1, 4, 20), (2, 6, 60), (4, 7, 30)]
# (1, 4, 20) + (4, 7, 30)
Expected Output: 50

"""

from typing import List, Tuple
from collections import defaultdict


def schedule1(jobs: List[Tuple[int]]) -> int:
    mp = defaultdict(bool)
    jobs = [(profit, deadline) for deadline, profit in jobs]
    jobs.sort(reverse=True)
    total_profit = 0
    for profit, deadline in jobs:
        if deadline not in mp:
            total_profit+=profit
            mp[deadline] = True
    print(total_profit)



def schedule2(jobs: List[Tuple[int]]) -> Tuple[int]:
    mp = defaultdict(bool)
    jobs = [(profit, deadline) for deadline, profit in jobs]
    jobs.sort(reverse=True)
    print(jobs)
    total_profit = 0
    job = 0
    for profit, deadline in jobs:
        if deadline not in mp:
            total_profit+=profit
            mp[deadline] = True
            job+=1
    print(mp)
    print(total_profit, job, )

def schedule3(jobs: List[int], deadline: List[int]) -> int:
    ...


def schedule4(jobs: List[int], deadline: List[int]) -> int:
    ...


schedule2([(2, 100), (1, 19), (2, 27), (1, 25), (3, 15)])