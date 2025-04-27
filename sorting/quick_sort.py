'''

Quick sort algo: first take pivot element (mainly the middle element)
then partition the array by pivot element
recursively call for left and right part 
Best case scenario TC: O(nlogn)
WORSE case Scenario TC: O(n**2)
'''


class QuickSort:

    def __init__(self, nums):
        self.nums = nums


    def _partition(self, l, h):
        pivot = self.nums[l]
        i = l; j = h
        while i < j:
            while self.nums[i] <= pivot and i < h:
                i+=1
            
            while self.nums[j] > pivot and j > l:
                j-=1
            
            if (i < j):
                self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        self.nums[l], self.nums[j] = self.nums[j], self.nums[l]
        return j
        

    def _sort(self, l, h):
        if l < h:
            j = self._partition(l, h)
            self._sort(l ,j)
            self._sort(j+1, h)


    def sort(self):
        self._sort(0, len(self.nums)-1)
        

nums = [9, 3, 7, 5, 6, 4, 8, 2]
QuickSort(nums).sort()
print(nums)