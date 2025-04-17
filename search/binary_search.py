'''
Resources
More abstract template for binary search: https://leetcode.com/problems/koko-eating-bananas/solutions/769702/python-clear-explanation-powerful-ultimate-binary-search-template-solved-many-problems
'''

def binary_search(nums, target):
    i = 0
    j = len(nums) - 1
    while i <= j:
        mid = i + (j - i) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            j = mid - 1
        else:
            i = mid + 1
    
    return -1


def search_in_rotated_array(nums, target):
    '''
    Initution first find the sorted part of the array
    which either left or right 
    for left to be sorted part mid element must be greator than or equal to left part
    '''
    i = 0
    j = len(nums) - 1
    while i <= j:
        mid = i + (j - i) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[i]:
            if target >= nums[i] and target <= nums[mid]:
                j = mid - 1
            else:
                i = mid+1
        else:
            if target <= nums[j] and target >= nums[mid]:
                i = mid+1
            else:
                j = mid - 1

    return -1


def search_in_rotated_array_dup(nums, target):
    '''
    Q: What if array have duplicate we need to return left most or right most index of the target ?
    we will use the same code for searching the rotated array instead we keep searching to left most side
    but due to duplicate sometime we cannot decide sorted part (nums[i] == nums[mid] == nums[j] this condition) of the array so we shrink both from left and right
    '''
    i = 0
    j = len(nums) - 1
    result = -1
    while i <= j:
        mid = i + (j - i) // 2
        if nums[mid] == target:
            result = mid
            j = mid - 1
        elif nums[i] == nums[mid] == nums[j]:
            i += 1
            j -= 1
        elif nums[mid] >= nums[i]:
            if target >= nums[i] and target <= nums[mid]:
                j = mid - 1
            else:
                i = mid+1
        else:
            if target <= nums[j] and target >= nums[mid]:
                i = mid+1
            else:
                j = mid - 1

    return result
    

print(search_in_rotated_array_dup([1, 0, 1,1,1], 1))