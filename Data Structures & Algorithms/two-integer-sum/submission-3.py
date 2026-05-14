class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #every input has only 1 pair that is correct
        for i in range(0, len(nums)):
            need = target - nums[i]

            for j in range(i+1, len(nums)):
                if nums[j] == need:
                    return [i,j]