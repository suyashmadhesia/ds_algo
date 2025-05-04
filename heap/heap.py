from collections import deque

class Heap:
    '''
    Max Heap
    '''
    '''
    if node is at index: i
    left child is at index = 2i+1
    right child is at index = 2(i+1)
    its parent is at math.floor((i-1)/2)

    insertion in heap takes O(logn)
    deletion takes O(logn)
    '''

    def __init__(self, elements=[]):
        self._list = deque(elements)
        self._len = len(self._list)
        self._left = lambda k: 2 * k + 1
        self._right = lambda k: 2 * k + 2
        self._parent = lambda k: (k - 1) // 2
        self._heapify()

    def __iter__(self):
        for i in self._list:
            yield i


    def __len__(self):
        return self._len

    def __str__(self):
        return f"<Heap{[i for i in self._list]}>"

    def _swap(self, i, j):
        self._list[i], self._list[j] = self._list[j], self._list[i]

    def _sift_down(self, i):
        while True:
            largest = i
            left = self._left(i)
            right = self._right(i)

            if left < self._len and self._list[left] > self._list[largest]:
                largest = left
            if right < self._len and self._list[right] > self._list[largest]:
                largest = right

            if largest == i:
                break

            self._swap(i, largest)
            i = largest


    def _heapify(self):
        for i in range(self._len // 2 - 1, -1, -1):
            self._sift_down(i)


    def push(self, element):
        self._list.append(element)
        self._len += 1
        curr_index = self._len - 1
        parent_index = self._parent(curr_index)
        while self._list[curr_index] > self._list[parent_index]:
            self._swap(curr_index, parent_index)
            curr_index = parent_index
            parent_index = self._parent(curr_index)
            if curr_index == -1 or parent_index == -1:
                break

    def pop(self):
        if self._len == 0:
            raise "Empty heap unable to pop"
        self._swap(0, self._len-1)
        value = self._list.pop()
        self._len-=1
        self._sift_down(0)
        return value
        



# heap = Heap([])

# res = [80, 60, 50, 30, 20, 16, 13, 8]
# while res:
#     heap.push(res.pop())

# res = []
# print(heap)

# while heap:
#     res.append(heap.pop())

# print(res)
    

    