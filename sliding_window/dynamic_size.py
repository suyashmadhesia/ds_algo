"""
VARIABLE-SIZE SLIDING WINDOW
============================

Use this family of patterns when the window length is NOT given.

Two pointers:
    left  -> start of the current window
    right -> end of the current window

The window expands by moving `right`. Depending on the objective, we
shrink it by moving `left`.

IMPORTANT:
    Ordinary expand/shrink sliding-window logic relies on being able
    to restore the condition by moving the left boundary. For sum-based
    windows, the common templates below require non-negative numbers.
    Negative numbers can break that monotonic behavior.

Main patterns:
    A. Longest valid window       -> shrink WHILE invalid
    B. Shortest valid window      -> shrink WHILE valid
    C. Count windows at most K    -> add (right - left + 1)
    D. Exactly K                  -> atMost(K) - atMost(K - 1)
    E. Frequency-based windows    -> maintain a hashmap / counter
    F. Special optimized window   -> historical max frequency (LC 424)
"""

from collections import Counter, deque
from typing import List


# ---------------------------------------------------------------------
# A. LONGEST WINDOW THAT SATISFIES A CONDITION
# ---------------------------------------------------------------------
def longest_subarray_sum_at_most_k(nums: List[int], k: int) -> int:
    """
    Find the longest contiguous subarray with sum <= k.

    ASSUMPTION: nums contains non-negative numbers.
    Why? Adding an element cannot decrease the sum, and removing an
    element cannot increase it. This makes the expand/shrink strategy
    valid.

    Pattern:
        Expand right.
        WHILE invalid: remove nums[left], then increment left.
        Update the maximum length.

    Time: O(n), Space: O(1)
    """
    left = 0
    window_sum = 0
    best = 0

    for right, value in enumerate(nums):
        window_sum += value

        # Keep shrinking until the window becomes valid.
        while left <= right and window_sum > k:
            window_sum -= nums[left]
            left += 1

        best = max(best, right - left + 1)

    return best


# ---------------------------------------------------------------------
# B. SHORTEST WINDOW THAT SATISFIES A CONDITION
# ---------------------------------------------------------------------
def min_subarray_len(target: int, nums: List[int]) -> int:
    """
    LeetCode 209: Minimum Size Subarray Sum.

    Find the shortest contiguous subarray whose sum >= target.

    ASSUMPTION: nums contains positive numbers (the standard LC 209
    constraints). With negative numbers, use a different approach.

    Pattern:
        Expand right.
        WHILE valid: record the length, then shrink from the left.

    Time: O(n), Space: O(1)
    """
    left = 0
    window_sum = 0
    best = float("inf")

    for right, value in enumerate(nums):
        window_sum += value

        # While the current window reaches the target, try to make it
        # shorter by removing elements from the left.
        while window_sum >= target:
            best = min(best, right - left + 1)
            window_sum -= nums[left]
            left += 1

    return 0 if best == float("inf") else best


# ---------------------------------------------------------------------
# C. LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
# ---------------------------------------------------------------------
def length_of_longest_substring(s: str) -> int:
    """
    LeetCode 3.

    Condition: every character in the current window must be unique.

    When the newly added character appears more than once, shrink until
    its frequency returns to one.

    Time: O(n), Space: O(min(n, alphabet_size))
    """
    left = 0
    freq = {}
    best = 0

    for right, char in enumerate(s):
        freq[char] = freq.get(char, 0) + 1

        while freq[char] > 1:
            outgoing = s[left]
            freq[outgoing] -= 1
            if freq[outgoing] == 0:
                del freq[outgoing]
            left += 1

        best = max(best, right - left + 1)

    return best


# ---------------------------------------------------------------------
# D. LONGEST SUBSTRING WITH AT MOST K DISTINCT CHARACTERS
# ---------------------------------------------------------------------
def longest_substring_at_most_k_distinct(s: str, k: int) -> int:
    """
    Condition: the window may contain at most k distinct characters.

    The hashmap stores frequencies. Its length is the number of
    distinct characters currently in the window.

    Time: O(n), Space: O(alphabet_size)
    """
    if k <= 0:
        return 0

    left = 0
    freq = {}
    best = 0

    for right, char in enumerate(s):
        freq[char] = freq.get(char, 0) + 1

        while len(freq) > k:
            outgoing = s[left]
            freq[outgoing] -= 1

            if freq[outgoing] == 0:
                del freq[outgoing]

            left += 1

        best = max(best, right - left + 1)

    return best


# ---------------------------------------------------------------------
# E. LONGEST REPEATING CHARACTER REPLACEMENT
# ---------------------------------------------------------------------
def character_replacement(s: str, k: int) -> int:
    """
    LeetCode 424.

    Find the longest substring that can be made of one repeated
    character using at most k replacements.

    Key observation:
        replacements_needed = window_size - max_frequency

    If this is greater than k, shrink the window.

    IMPORTANT OPTIMIZATION:
        `max_freq` is the highest frequency observed while expanding.
        We deliberately do NOT decrease it when the left side shrinks.
        It can therefore be stale relative to the current window.

        This stale value is safe for this particular algorithm: the
        window length never decreases (we shrink at most once for each
        right expansion), and the stale maximum can delay shrinking but
        cannot create a larger answer than a feasible window length.
        Do not blindly reuse this optimization for unrelated problems.

    We use IF rather than WHILE: after each right expansion, shrink at
    most once, keeping the window length constant or increasing it.

    Time: O(n), Space: O(1) for uppercase English letters.
    """
    left = 0
    freq = {}
    max_freq = 0
    best = 0

    for right, char in enumerate(s):
        freq[char] = freq.get(char, 0) + 1
        max_freq = max(max_freq, freq[char])

        window_size = right - left + 1
        replacements_needed = window_size - max_freq

        if replacements_needed > k:
            freq[s[left]] -= 1
            left += 1

        best = max(best, right - left + 1)

    return best


# ---------------------------------------------------------------------
# F. COUNT SUBARRAYS WITH AT MOST K DISTINCT VALUES
# ---------------------------------------------------------------------
def at_most_k_distinct(nums: List[int], k: int) -> int:
    """
    Count contiguous subarrays containing at most k distinct values.

    Key counting idea:
        Once [left, right] is valid, every subarray ending at `right`
        and starting at any index from `left` through `right` is valid.

        Number of such subarrays = right - left + 1.

    Time: O(n), Space: O(number of distinct values in the window).
    """
    if k < 0:
        return 0

    left = 0
    freq = {}
    count = 0

    for right, value in enumerate(nums):
        freq[value] = freq.get(value, 0) + 1

        while len(freq) > k:
            outgoing = nums[left]
            freq[outgoing] -= 1

            if freq[outgoing] == 0:
                del freq[outgoing]

            left += 1

        # Count all valid subarrays that end at `right`.
        count += right - left + 1

    return count


# ---------------------------------------------------------------------
# G. EXACTLY K DISTINCT VALUES
# ---------------------------------------------------------------------
def exactly_k_distinct(nums: List[int], k: int) -> int:
    """
    LeetCode 992: Subarrays with K Different Integers.

    Identity:
        exactly(K) = atMost(K) - atMost(K - 1)

    Why it works:
        atMost(K) counts subarrays with 0, 1, ..., K distinct values.
        atMost(K-1) counts subarrays with 0, 1, ..., K-1 distinct values.
        Their difference leaves only those with exactly K.

    Time: O(n), Space: O(n) worst case due to frequency maps.
    """
    if k <= 0:
        return 0

    return at_most_k_distinct(nums, k) - at_most_k_distinct(nums, k - 1)


# ---------------------------------------------------------------------
# H. MINIMUM WINDOW SUBSTRING
# ---------------------------------------------------------------------
def min_window(s: str, t: str) -> str:
    """
    LeetCode 76.

    Return the smallest substring of s containing all characters of t,
    including duplicate character requirements.

    `need`: required frequency of each character in t.
    `window`: current frequency inside the sliding window.
    `formed`: number of distinct required characters whose required
              frequency has been met.

    Once formed == required, the window contains everything needed.
    Shrink it while it remains valid, recording the smallest window.

    Time: O(len(s) + len(t)), Space: O(character_set_size).
    """
    if not s or not t:
        return ""

    need = Counter(t)
    window = {}
    required = len(need)
    formed = 0

    left = 0
    best_length = float("inf")
    best_start = 0

    for right, char in enumerate(s):
        window[char] = window.get(char, 0) + 1

        # A required character becomes satisfied exactly when its
        # window frequency reaches the required frequency.
        if char in need and window[char] == need[char]:
            formed += 1

        # All distinct character requirements are currently satisfied.
        while formed == required:
            current_length = right - left + 1

            if current_length < best_length:
                best_length = current_length
                best_start = left

            outgoing = s[left]
            window[outgoing] -= 1

            # Removing this character made one requirement unsatisfied.
            if outgoing in need and window[outgoing] < need[outgoing]:
                formed -= 1

            left += 1

    if best_length == float("inf"):
        return ""

    return s[best_start:best_start + best_length]


# ---------------------------------------------------------------------
# I. MONOTONIC DEQUE: MAXIMUM IN EVERY FIXED-SIZE WINDOW
# ---------------------------------------------------------------------
def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """
    LeetCode 239.

    This is a fixed-size window combined with a monotonic deque.

    The deque stores INDICES, not values, and their corresponding values
    are in decreasing order. Therefore, the front is always the maximum.

    Steps:
        1. Remove the front index if it has left the window.
        2. Remove smaller/equal values from the back: they can never
           become the maximum while the newer, larger value remains.
        3. Add the current index.
        4. Once the first full window exists, read the maximum at front.

    Time: O(n), Space: O(k).
    """
    if k <= 0 or k > len(nums):
        return []

    dq = deque()
    answer = []

    for right, value in enumerate(nums):

        # Remove indices that are no longer inside [right-k+1, right].
        while dq and dq[0] <= right - k:
            dq.popleft()

        # Keep values in decreasing order from front to back.
        while dq and nums[dq[-1]] <= value:
            dq.pop()

        dq.append(right)

        # A complete window exists once right reaches k-1.
        if right >= k - 1:
            answer.append(nums[dq[0]])

    return answer


# ---------------------------------------------------------------------
# J. GENERIC VARIABLE-SIZE TEMPLATES (PSEUDOCODE)
# ---------------------------------------------------------------------
def longest_window_template(items):
    """
    LONGEST valid window:

        left = 0
        for right in range(len(items)):
            add(items[right])

            while window_is_invalid:
                remove(items[left])
                left += 1

            answer = max(answer, right - left + 1)

    Use `while` because one removal may not restore validity.
    """
    raise NotImplementedError("Replace the condition and state for your problem")


def shortest_window_template(items):
    """
    SHORTEST valid window:

        left = 0
        for right in range(len(items)):
            add(items[right])

            while window_is_valid:
                answer = min(answer, right - left + 1)
                remove(items[left])
                left += 1

    Shrink while valid because every smaller valid window is a candidate.
    """
    raise NotImplementedError("Replace the condition and state for your problem")


if __name__ == "__main__":
    print("Longest sum <= 5:", longest_subarray_sum_at_most_k([2, 1, 3, 2, 1, 1], 5))
    print("Minimum sum >= 7:", min_subarray_len(7, [2, 3, 1, 2, 4, 3]))
    print("Longest unique substring:", length_of_longest_substring("abcabcbb"))
    print("At most 2 distinct:", longest_substring_at_most_k("eceba", 2))
    print("Character replacement:", character_replacement("AABABBA", 1))
    print("Exactly 2 distinct:", exactly_k_distinct([1, 2, 1, 2, 3], 2))
    print("Minimum window:", min_window("ADOBECODEBANC", "ABC"))
    print("Sliding window maximum:", max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))
