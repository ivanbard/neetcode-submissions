class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # return all unique number combinations that add to target
        # can reuse numbers inf times
        # unique number combos have differing num frequencies
        result, subset = [], []

        def dfs(i, total):
            # check if end of array
            if i >= len(nums) or total > target:
                return
            
            if total == target:
                result.append(subset.copy())
                return

            # check next possibility WITH elem i included
            subset.append(nums[i])
            dfs(i, total + nums[i])

            # do next possibility WITHOUT elem i included
            subset.pop()
            dfs(i+1, total)

        dfs(0, 0)
        return result
