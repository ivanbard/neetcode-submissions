class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # cells cannot be used more than once in a word
        if board is None:
            return False
        curr = []
        visited = set()
        #x, y = 0, 0
        found = False

        def dfs(x, y):
            nonlocal found

            # stop if cell already in path or word doesn't match
            if (x, y) in visited or board[x][y] != word[len(curr)]:
                return

            visited.add((x, y))
            curr.append(board[x][y])

            if len(curr) == len(word):
                found = True
            else:
                # explore down, right, up and left options
                if x + 1 < len(board):
                    dfs(x + 1, y)
                if y + 1 < len(board[0]):
                    dfs(x, y + 1)
                if x - 1 >= 0:
                    dfs(x - 1, y)
                if y - 1 >= 0:
                    dfs(x, y - 1)

            curr.pop()
            visited.remove((x, y))

        for x in range(len(board)):
            for y in range(len(board[0])):
                dfs(x,y)
                if found:
                    return True
        return False