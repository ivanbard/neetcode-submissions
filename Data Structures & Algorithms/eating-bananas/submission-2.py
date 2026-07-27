import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h = number of hours to eat bananas
        # piles[i] = number of bananas at ith pile
        # find and return minimual k = bananas per hour

        low = 1
        high = max(piles)
        result = high

        while low <= high:
            k = (low + high)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)

            if hours <= h:
                result = min(result, k)
                high = k-1
            else:
                low = k+1

        return result