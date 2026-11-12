class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # iterate thorugh all neighbours of first 1
        # mark those part of group so they aren't reused
        num_islands = 0

        def dfs(row, col):
            # if current is water or out of bounds:
            if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == "0"):
                return

            # set current to 0 so it is not visited again
            grid[row][col] = "0"
            # explore neighbouring cells
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    # increment number of islands in main loop
                    num_islands += 1
                    dfs(i,j)

        return num_islands