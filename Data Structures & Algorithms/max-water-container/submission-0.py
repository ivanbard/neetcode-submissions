class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = (len(heights)) - 1
        curr_max = 0

        while i < j:
            area = 0
            length = j-i

            area = length * (min(heights[i], heights[j]))
            if area > curr_max:
                curr_max = area

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return curr_max