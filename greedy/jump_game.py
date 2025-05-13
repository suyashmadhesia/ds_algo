from typing import List

class Solution:
    """
    Jump Game II - Minimum number of jumps to reach the end

    Idea:
    - Use a greedy approach to always jump to the farthest reachable index.
    - We maintain a window [l, r] which represents the range of indices we can reach with the current number of jumps.
    - In each iteration, we compute the farthest index we can reach in the next jump from within [l, r].
    - Once we've considered all positions in the current window, we move to the next window (next jump) and repeat.
    """
    def jump(self, nums: List[int]) -> int:
        l = 0          # Left bound of current jump range
        r = 0          # Right bound of current jump range
        jumps = 0      # Total jumps made
        n = len(nums)

        while r < n - 1:
            # Track the farthest index we can reach in the next jump
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])

            # Move to the next window
            l = r + 1
            r = farthest
            jumps += 1

        return jumps
    

    def jumpI(self, nums) -> bool:
        """
        Jump Game I - Determine if you can reach the last index

        Idea:
        - Greedily track the farthest index you can reach at every position.
        - If at any point, the current index `i` is greater than `max_range`, 
        it means we're stuck and can't move further — return False.
        - If we make it through the entire array, return True.
        """
        max_range = 0  # Tracks the farthest index we can reach

        for i, val in enumerate(nums):
            if i > max_range:
                # Current position is unreachable
                return False
            max_range = max(max_range, i + val)  # Update max reachable index

        return True
