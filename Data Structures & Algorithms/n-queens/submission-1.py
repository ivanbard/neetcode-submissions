
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #return array of strings
        # each string in array represents a row on the board
        results = []
        board = [["."] * n for i in range(n)]

        cols = set()
        posDiag = set()  # row + col
        negDiag = set()  # row - col

        def isSafe(r: int, c: int):
            if c in cols or (r + c) in posDiag or (r - c) in negDiag:
                return False
            return True

        def backtrack(row):
            if row == n:
                copy = ["".join(r) for r in board]
                results.append(copy)
                return

            for c in range(n):
                if isSafe(row, c):
                    board[row][c] = "Q"

                    # mark column and diagonals as occupied
                    cols.add(c)
                    posDiag.add(row + c)
                    negDiag.add(row - c)

                    backtrack(row+1)

                    # "pop" current queen for next backtrack iter
                    board[row][c] = "."
                    cols.remove(c)
                    posDiag.remove(row + c)
                    negDiag.remove(row - c)

            # 1 queen per row OR col

        backtrack(0)
        return results
