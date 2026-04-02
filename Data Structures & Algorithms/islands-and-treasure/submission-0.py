# we perform bfs when we come across a cell with INF value
# we stop when we reach a treasure cell
# keep track of visited cells
# if we come across a cell with value not 2147483647 that is 
# the nearest treasure for the cell has already been calculated
# we can add the use the precalculated value

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def bfs(row, col):
            q = deque([(row, col)])
            v = set((row, col))
            cnt, prev_cnt = 1, 2147483647

            direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direc:
                        nr, nc = dr + r, dc + c
                        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in v and grid[nr][nc] != -1:
                            if grid[nr][nc] == 0:
                                return min(cnt, prev_cnt)
                            elif grid[nr][nc] == 2147483647:
                                q.append((nr, nc))
                            else:
                                prev_cnt = min(prev_cnt, cnt + grid[nr][nc])
                        
                        v.add((nr, nc))

                    
                cnt += 1
            
            return 2147483647 if prev_cnt == 2147483647 else prev_cnt



        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2147483647:
                    grid[r][c] = bfs(r, c)
        