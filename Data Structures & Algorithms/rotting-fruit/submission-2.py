# use bfs to solve this problem, as the min number of mins can be found levelwise
# we put all the rotten oranges in a queue and then move one level at a time
# when the queue is empty we stop, make sure that each cell is visited once
# change fresh to rotten at the end

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def bfs(q):
            nonlocal fresh_cnt

            tot_min = -1
            fresh_here = 0

            direc = [(0, -1), (-1, 0), (1, 0), (0, 1)]
            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direc:
                        nr, nc = dr + r, dc + c
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                            fresh_here += 1
                            grid[nr][nc] = 2
                            q.append((nr, nc))
                tot_min += 1
            
            return tot_min if fresh_here == fresh_cnt else -1


        q = deque()
        fresh_cnt = 0

        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_cnt += 1
        
        if fresh_cnt == 0:
            return 0
        return bfs(q)