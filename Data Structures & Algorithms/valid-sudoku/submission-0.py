class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1 to 1 conversion between array and sudoku board
        # each row, column, and 3x3 box must contain digits 1-9 without dupes
        # Board does NOT need to be full or solvable to be valid!!!

        # use hash set for every row and every column to check dupes

        for i in range(len(board)):
            col_seen = set()
            row_seen = set()
            for j in range(len(board[i])):
                val_row = board[i][j]
                if val_row != ".":
                    if val_row in row_seen:
                        return False
                    row_seen.add(val_row)

                val_col = board[j][i]
                if val_col != ".":
                    if val_col in col_seen:
                        return False
                    col_seen.add(val_col)

        for bi in range(0, 9, 3):
            for bj in range(0, 9, 3):
                box_seen = set()
                for r in range(bi, bi + 3):
                    for c in range(bj, bj + 3):
                        val = board[r][c]
                        if val != ".":
                            if val in box_seen:
                                return False
                            box_seen.add(val)



        return True