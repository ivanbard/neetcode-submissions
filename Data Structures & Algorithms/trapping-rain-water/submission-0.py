class Solution:
    def trap(self, height: List[int]) -> int:
        # need to keep track of "walls" on side of each water block
        # l = 0
        # r = len(height) - 1
        trapped = 0

        left_max = [0] * len(height)
        right_max = [0] * len(height)

        #tallest wall seen from left so far
        left_max[0] = height[0]
        for i in range(1,len(height)):
            left_max[i] = max(left_max[i-1], height[i])

        # tallest wall seen from right so far
        right_max[len(height) - 1] = height[len(height)-1]
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])

        # sum
        for i in range(len(height)):
            trapped += min(left_max[i], right_max[i]) - height[i]

        return trapped