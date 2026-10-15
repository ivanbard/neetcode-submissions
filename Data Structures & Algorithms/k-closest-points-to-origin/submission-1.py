import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = x**2 + y**2
            heap.append((dist, x, y))

        heapq.heapify_max(heap)

        while len(heap) > k:
            heapq.heappop_max(heap)

        return [[x, y] for dist, x, y in heap]