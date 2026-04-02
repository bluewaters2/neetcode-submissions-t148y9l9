class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(q, s):
            direc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            while q:
                r, c = q.popleft()
                for dr, dc in direc:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in s and heights[nr][nc] >= heights[r][c]:
                        q.append((nr, nc))
                        s.add((nr, nc))



        rows, cols = len(heights), len(heights[0])

        atlantic, pacific = deque(), deque()
        s1, s2 = set(), set()

        for i in range(rows):
            atlantic.append((i, cols-1))
            pacific.append((i, 0))
            s1.add((i, 0))
            s2.add((i, cols-1))
        
        for i in range(cols):
            atlantic.append((rows-1, i))
            pacific.append((0, i))
            s1.add((0, i))
            s2.add((rows-1, i))
        
        dfs(pacific, s1)
        dfs(atlantic, s2)

        return list(s1.intersection(s2))