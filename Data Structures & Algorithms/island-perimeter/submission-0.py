# we use dfs to find the perimeter of the land present
# since there is only one land present, we start from one cell and call dfs on it
# when a land cell is visited, we check all 4 neighbours for that cell 
# and if neighbor is land then we subtract from the 4, check both for land and visited cell
# visited cell helps to make sure no cell is visited more than once.  

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] == 0:
                return 1
            
            if (i, j) in visit:
                return 0
            
            visit.add((i, j))
            peri = dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            return peri
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    return dfs(i, j)
        
        return 0