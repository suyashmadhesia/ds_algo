import random


def quickselect(nums, k):
    """
        Step-by-Step Working:
        Find the k-th largest → means we actually find (len - k)-th smallest. for smalled k = k-1 index
        Here, len(nums) = 8
        k=3 → we find (8-3) = 5-th smallest.
        Now run QuickSelect to find the 5th smallest element.
        Partitioning divides array into:
        Left part (elements ≤ pivot)
        Pivot at correct position
        Right part (elements > pivot)
        Depending on pivot position:
        If pivot_index == k: done, return.
        If pivot_index < k: search right.
        If pivot_index > k: search left.
    """
    k = len(nums) - k  # convert to k-th smallest

    def partition(l, r):
        pivot = nums[r]
        i = l
        for j in range(l, r):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    l, r = 0, len(nums) - 1
    while l <= r:
        pivot_index = partition(l, r)
        if pivot_index == k:
            return nums[pivot_index]
        elif pivot_index < k:
            l = pivot_index + 1
        else:
            r = pivot_index - 1


# Example usage
nums = [7, 2, 1, 8, 6, 3, 5, 4]
k = 3
print(quickselect(nums, k))  # Output: 6
