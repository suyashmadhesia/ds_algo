'''
Merge sort first divide list into smaller list then merge them
TC: O(nlogn)
SC: O(n) where n is recursive stack 
'''


class MergeSort:

    def __init__(self, nums):
        self.nums = nums

    
    def _merge(self, low, mid, high):
        i = low
        j = mid+1
        if self.nums[mid] <= self.nums[j]:
            return
        while i <= mid and j <= high:
            if self.nums[i] <= self.nums[j]:
                i+=1
            else:
                right_val = self.nums[j]
                index = j
                while index != i:
                    self.nums[index] = self.nums[index-1]
                    index -= 1
                self.nums[i] = right_val
                i+=1
                mid+=1
                j+=1

    def _sort(self, i, j):
        if i < j:
            mid = i + (j-i)//2
            self._sort(i, mid)
            self._sort(mid+1, j)
            self._merge(i, mid, j)

    def sort(self):
        self._sort(0, len(self.nums)-1)



nums = [9, 3, 7, 5, 6, 4, 8, 2]
MergeSort(nums).sort()
print(nums)