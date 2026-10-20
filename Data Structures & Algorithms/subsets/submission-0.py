class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return 

            # include i in subset
            subset.append(nums[i])
            dfs(i + 1)

            # do not include i in subset
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return result