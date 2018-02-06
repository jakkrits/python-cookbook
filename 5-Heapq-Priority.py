import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums) # or make a copy -> heap = nums[:]
print(heap)
heap.heapify(heap)
print(heap)

class PriorityQueue:
    def __init__(self, *args, **kwargs):
        self._queue = []
        self._index = 0
