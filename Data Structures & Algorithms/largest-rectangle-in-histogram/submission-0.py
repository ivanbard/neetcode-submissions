class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # biggest rectangle will depend on the smallest bar in it
        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: #if top val in stack and height of it is greater than reached
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index

            stack.append((start, h)) #add the start index that we pushed all the way back

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area