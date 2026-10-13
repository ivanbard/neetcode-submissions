import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        self.k_val = k        
        # trim after heapifying too
        while len(self.min_heap) > self.k_val:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        # check if num elems in heap > k
        # remove those that exceed k elems
        while len(self.min_heap) > self.k_val:
            heapq.heappop(self.min_heap)

        return self.min_heap[0]