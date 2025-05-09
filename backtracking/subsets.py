from typing import List

class Solution:
    '''
    Function to find all subsets (the power set) of a list of unique integers.
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.temp = []  # Temporary list to build current subset
        self.ans = []   # Final list to store all subsets
        self.n = len(nums)

        def sub(i):
            # Always add a copy of the current subset
            self.ans.append(self.temp[:])
            # Try including each element from index i+1 onward
            for j in range(i + 1, self.n):
                self.temp.append(nums[j])  # Choose
                sub(j)                     # Explore
                self.temp.pop()            # Unchoose (backtrack)

        sub(-1)
        return self.ans
        

class Solution:
    '''
    Function to find all unique subsets from a list of integers that may contain duplicates.
    '''
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.temp = []  # Temporary list to build current subset
        self.ans = []   # Final list to store all unique subsets
        self.n = len(nums)
        nums.sort()     # Sort to group duplicates together

        def sub(i):
            # Always add a copy of the current subset
            self.ans.append(self.temp[:])
            # Explore all choices starting from index i
            for j in range(i, self.n):
                # Skip duplicates: if current is same as previous and at same level, skip
                if j > i and nums[j - 1] == nums[j]:
                    continue
                self.temp.append(nums[j])  # Choose
                sub(j + 1)                 # Explore
                self.temp.pop()            # Unchoose (backtrack)

        sub(0)
        return self.ans



        