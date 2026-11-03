class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, subset = [], []

        # func to check if string is palindrome
        def is_pal(text: str)->bool:
            return text==text[::-1]

        def dfs(start):
            # reached end of string
            if start == len(s):
                result.append(subset.copy())
                return

            for end in range(start, len(s)):
                # split substring
                piece = s[start:end +1]

                # if piece is palindrome add to subset and backtrack
                if is_pal(piece):
                    subset.append(piece)
                    dfs(end +1)
                    subset.pop()

        dfs(0)
        return result