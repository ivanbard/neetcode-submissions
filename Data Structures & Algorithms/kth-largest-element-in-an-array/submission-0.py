import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_elems = []
        for i in range(len(nums)):
            heapq.heappush(k_elems, nums[i])

            # if more than k elems, drop it
            if len(k_elems) > k:
                heapq.heappop(k_elems)

        return k_elems[0]