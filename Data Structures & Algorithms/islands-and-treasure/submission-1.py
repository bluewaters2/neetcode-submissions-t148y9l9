# we can apply bfs to find the distance to the nearest treasure chest
# we start bfs from the treasure chest and reach all the land cell
# this will be more efficient

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(q):
            visit = set()
            dist = 0
            direc = [(0, 1), (1, 0), (-1, 0), (0, -1)]

            while q:
                dist += 1
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direc:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 2147483647:
                            grid[nr][nc] = dist
                            q.append((nr, nc))
                            

        rows, cols = len(grid), len(grid[0])
        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        bfs(q)