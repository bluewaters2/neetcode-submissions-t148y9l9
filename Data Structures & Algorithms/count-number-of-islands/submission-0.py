# we iterate through the given grid and find the number of islands using dfs
# when we come across a land cell, dfs is performed and all the reachable land cells are changed to 0

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            return
        

        rows, cols = len(grid), len(grid[0])
        cnt = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    cnt += 1
                    dfs(r, c)
        
        return cnt