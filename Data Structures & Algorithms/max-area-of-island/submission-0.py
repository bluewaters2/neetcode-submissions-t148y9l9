# iterate through the given grid, find the areas of each using dfs

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c):
            curr_area = 1
            direc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
            stack = [(r, c)]
            grid[r][c] = 0

            while stack:
                row, col = stack.pop()
                for dr, dc in direc:
                    nr, nc = dr + row, dc + col
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        stack.append((nr, nc))
                        grid[nr][nc] = 0
                        curr_area += 1
            
            return curr_area
            
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r, c))
        
        return max_area