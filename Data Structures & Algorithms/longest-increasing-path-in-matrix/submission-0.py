# we can use dfs + memoization to calculate the longest increasing path in matrix

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def dfs(r, c, prev):
            if r < 0 or c < 0 or r >= rows or c >= cols or matrix[r][c] <= prev:
                return 0
            
            if store[r][c] != -1:
                return store[r][c]
            
            up = dfs(r - 1, c, matrix[r][c])
            down = dfs(r + 1, c, matrix[r][c])
            left = dfs(r, c - 1, matrix[r][c])
            right = dfs(r, c + 1, matrix[r][c])

            store[r][c] = max(up, down, left, right) + 1
            return store[r][c]

        rows, cols = len(matrix), len(matrix[0])
        ans = 0

        store = [[-1] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                ans = max(ans, dfs(row, col, -1))
        
        return ans