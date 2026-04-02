# we have to find the min path sum from (0, 0) to (rows-1, cols-1)
# can only move either down or right along its path
# use dp, a grid of the same size to store the subproblem values

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]

        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + grid[i][0] 
        
        for j in range(1, cols):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for r in range(1, rows):
            for c in range(1, cols):
                dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c]
        
        return dp[rows-1][cols-1]