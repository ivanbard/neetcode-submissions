class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # have a list sorted in increasing order
        # since one indexed??
        i = 0
        j = (len(numbers)-1)

        while i < j:
            #if numbers[i] > target or numbers[j] > target:
                #i += 1
                #j -= 1
            #else: 
            # move right pointer in until sum is <= target
            # move left pointer in until sum = target
            if (numbers[i] + numbers[j]) == target:
                return [i+1,j+1]  # Convert to 1-indexed
            if (numbers[i] + numbers[j]) > target:
                j -= 1
            if (numbers[i] + numbers[j]) < target:
                i += 1