class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find min in sorted array without iterating through it 
        left, right = 0, len(nums) - 1
        #smallest = nums[0]

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid +1
            else:
                right = mid

        return nums[left]