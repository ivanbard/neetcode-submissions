import heapq


class MedianFinder:
    # returning the middle value in a sorted list of ints
    # if num of elems in list is even, median is the avg of the two middle values

    def __init__(self):
        self.left = [] # to be max-heap
        self.right = [] # to be min-heap

    def addNum(self, num: int) -> None:
        # adds num to current list
        # IMPORTANT: num added should be put in sorted order in curr list
        heapq.heapify_max(self.left)
        heapq.heapify(self.right)

        if self.right and num > self.right[0]:
            heapq.heappush(self.right, num)
        else:
            heapq.heappush_max(self.left, num)

        # if diff in heap len > 1 we must rebalance
        if len(self.left) > len(self.right) + 1:
            temp = heapq.heappop_max(self.left)
            heapq.heappush(self.right, temp)
        elif len(self.right) > len(self.left) + 1:
            temp = heapq.heappop(self.right)
            heapq.heappush_max(self.left, temp)

    def findMedian(self) -> float:
        # returns median of ALL ELEMS SO FAR
        if len(self.right) == len(self.left):
            return (self.right[0] + self.left[0])/2
        elif len(self.left) > len(self.right):
            return self.left[0]
        else:
            return self.right[0]
