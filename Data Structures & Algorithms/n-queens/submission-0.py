class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        #return array of strings
        # each string in array represents a row on the board
        results = []
        board = [["."] * n for i in range(n)]

        def isSafe(r: int, c: int, board):
            # 1 queen per row OR col
            row = r - 1
            while row >= 0:
                if board[row][c] == "Q":
                    return False
                row -= 1

            row, col = r - 1, c - 1
            while row >= 0 and col >= 0:
                if board[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            row, col = r - 1, c + 1
            while row >= 0 and col < len(board):
                if board[row][col] == "Q":
                    return False
                row -= 1
                col += 1
            return True

        def backtrack(row):
            if row == n:
                copy = ["".join(r) for r in board]
                results.append(copy)
                return

            for c in range(n):
                if isSafe(row, c, board):
                    board[row][c] = "Q"
                    backtrack(row+1)
                    # "pop" current queen for next backtrack iter
                    board[row][c] = "."

        backtrack(0)
        return results