class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # return all unique number combinations that add to target
        # cannot reuse numbers
        result, subset = [], []
        candidates.sort()

        def dfs(i, total):
            if total == target:
                result.append(subset.copy())
                return
            # check if end of array
            if i >= len(candidates) or total > target:
                return

            # check next possibility WITH elem i included
            subset.append(candidates[i])
            dfs(i+1, total + candidates[i])

            # do next possibility WITHOUT elem i included
            subset.pop()
            # skip identical vals next to one another 
            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i+= 1
            dfs(i+1, total)

        dfs(0, 0)
        return result
