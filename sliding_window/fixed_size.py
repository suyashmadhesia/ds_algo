"""
FIXED-SIZE SLIDING WINDOW
=========================

Use this pattern when the window length K is given in the problem.

Core idea:
    1. Add the element at `right` to the window.
    2. When the window reaches size K, process it.
    3. Remove the element at `left`.
    4. Move `left` forward.

The window never grows beyond K after processing each complete window.

Typical problems:
    - Maximum sum of a subarray of size K
    - Maximum average of a subarray of size K
    - Find all anagrams / permutations (fixed-length frequency window)
    - Count fixed-size windows satisfying a condition

Complexity:
    Usually O(n) time because each element enters and leaves once.
"""

from collections import Counter
from typing import List


# ---------------------------------------------------------------------
# 1. BASIC TEMPLATE: fixed-size window with a running sum
# ---------------------------------------------------------------------
def max_sum_subarray_of_size_k(nums: List[int], k: int) -> int:
    """
    Return the maximum sum among all contiguous subarrays of length k.

    Example:
        nums = [2, 1, 5, 1, 3, 2], k = 3
        Windows: [2,1,5] -> 8
                 [1,5,1] -> 7
                 [5,1,3] -> 9
                 [1,3,2] -> 6
        Answer: 9

    Time:  O(n)
    Space: O(1)
    """
    if k <= 0 or k > len(nums):
        raise ValueError("k must be between 1 and len(nums)")

    left = 0
    window_sum = 0
    best = float("-inf")

    for right in range(len(nums)):
        # 1) Include the new rightmost element.
        window_sum += nums[right]

        # 2) Process the window as soon as it has exactly k elements.
        if right - left + 1 == k:
            best = max(best, window_sum)

            # 3) Prepare for the next window:
            #    remove the outgoing leftmost element, then move left.
            window_sum -= nums[left]
            left += 1

    return best


# ---------------------------------------------------------------------
# 2. FIXED-SIZE WINDOW: maximum average
# ---------------------------------------------------------------------
def find_max_average(nums: List[int], k: int) -> float:
    """
    LeetCode 643: Maximum Average Subarray I.

    The window mechanics are identical to the running-sum example.
    We only divide the best sum by k at the end.

    Time: O(n), Space: O(1)
    """
    if k <= 0 or k > len(nums):
        raise ValueError("k must be between 1 and len(nums)")

    left = 0
    window_sum = 0
    best_sum = float("-inf")

    for right, value in enumerate(nums):
        window_sum += value

        if right - left + 1 == k:
            best_sum = max(best_sum, window_sum)
            window_sum -= nums[left]
            left += 1

    return best_sum / k


# ---------------------------------------------------------------------
# 3. FIXED-SIZE WINDOW: frequency map for strings
# ---------------------------------------------------------------------
def find_anagrams(s: str, p: str) -> List[int]:
    """
    LeetCode 438: Find All Anagrams in a String.

    Every anagram of p has exactly len(p) characters. Therefore, the
    window size is fixed at len(p).

    This version compares frequency dictionaries for clarity.
    For lowercase English letters, a 26-element array can optimize it.

    Time: O(n * alphabet_size) in the worst case for dictionary comparison.
    Space: O(alphabet_size)
    """
    k = len(p)
    if k == 0 or k > len(s):
        return []

    target_freq = Counter(p)
    window_freq = Counter()
    answer = []
    left = 0

    for right, char in enumerate(s):
        # Add the incoming character.
        window_freq[char] += 1

        # If the window is too large, remove its leftmost character.
        if right - left + 1 > k:
            outgoing = s[left]
            window_freq[outgoing] -= 1

            if window_freq[outgoing] == 0:
                del window_freq[outgoing]

            left += 1

        # Compare only once the window has exactly k characters.
        if right - left + 1 == k and window_freq == target_freq:
            answer.append(left)

    return answer


# ---------------------------------------------------------------------
# 4. GENERAL FIXED-SIZE TEMPLATE
# ---------------------------------------------------------------------
def fixed_window_template(nums: List[int], k: int) -> None:
    """
    Copy this structure and replace `process_window()` with the metric
    your problem asks for (sum, product, count, frequency, etc.).
    """
    left = 0
    state = 0  # Replace with the data you need to maintain.

    for right in range(len(nums)):
        # ADD nums[right] to the window state.
        # Example for sum: state += nums[right]
        pass

        if right - left + 1 == k:
            # PROCESS the current window here.
            # Example: update an answer using `state`.
            pass

            # REMOVE nums[left] before moving the left boundary.
            # Example for sum: state -= nums[left]
            pass
            left += 1


if __name__ == "__main__":
    print("Maximum sum:", max_sum_subarray_of_size_k([2, 1, 5, 1, 3, 2], 3))
    print("Maximum average:", find_max_average([1, 12, -5, -6, 50, 3], 4))
    print("Anagram starting indices:", find_anagrams("cbaebabacd", "abc"))
