class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximums = []
        left = 0

        for right in range(k, len(nums) + 1):
            window_max = float('-inf')
            for j in range(left, right):
                window_max = max(window_max, nums[j])
            
            maximums.append(window_max)
            left += 1
        
        return maximums