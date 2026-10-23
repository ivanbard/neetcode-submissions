class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result, subset = [], []
        added = [False] * len(nums)

        def dfs():
            if len(subset) >= len(nums):
                result.append(subset.copy())
                return

            for i in range(len(nums)):
                if added[i]:
                    continue

                # choose unpicked elem
                subset.append(nums[i])
                added[i] = True

                # find all completions of this choice
                dfs()

                #undo so loop can try another result
                subset.pop()
                added[i] = False

        dfs()
        return result