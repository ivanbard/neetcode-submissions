class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # n cars travelling in same direction on highway to destination 'target'
        # if a faster-moving car catches up to slower one, it cant pass it
        # this creates a fleet, or a stack of cars
        fleets = []
        pair = [[p, s] for p, s in zip(position, speed)]

        for p, s in sorted(pair)[::-1]: # for the reverse sorted order,closest car to target first
            fleets.append((target - p) / s)
            # if more than one car in stack and 2nd cars time is less than first
            if len(fleets) >= 2 and fleets[-1] <= fleets[-2]:
                fleets.pop() #cars collide, they create a fleet


        return len(fleets)