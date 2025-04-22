'''
Finding square root of x using binary search!!
'''

def find_sqrt_with_binary_search(num): # only for integers
    i = 1
    j = num

    while i < j:
        mid = i + (j - i) // 2
        if mid**2 == num:
            return mid
        elif mid**2 < num:
            i = mid+1
        else:
            j = mid
    
    return -1


def find_sqrt_with_precision(x, precision=1e-9):
    if x < 0:
        return None  # square root not defined for negative numbers

    low = 0
    high = x if x >= 1 else 1  # For numbers less than 1, set high = 1

    while high - low > precision:
        mid = (low + high) / 2
        if mid * mid < x:
            low = mid
        else:
            high = mid

    return (low + high) / 2

print(find_sqrt_with_precision(16))