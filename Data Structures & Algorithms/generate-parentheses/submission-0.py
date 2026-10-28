class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # num of closing brackets must equal to num of opening brackets
        results, subset = [], []
        open, close = 0, 0

        def dfs():
            nonlocal open, close
            if len(subset)== 2*n:
                results.append("".join(subset.copy()))
                return

            # start with testing open case
            if open < n:
                subset.append('(')
                open += 1
                dfs()

                # remove open to allow other cases to test
                open-= 1
                subset.pop()

            # check if we can stil add a close
            if close < open:
                subset.append(')')
                close += 1
                dfs()

                close -= 1
                subset.pop()

        dfs()
        return results