class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        
        GUARD = 1
        WALL = 2
        GUARDED = 3
        
        for r, c in guards:
            grid[r][c] = GUARD
        
        for r, c in walls:
            grid[r][c] = WALL
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for gr, gc in guards:
            for dr, dc in directions:
                r, c = gr + dr, gc + dc
                while 0 <= r < m and 0 <= c < n:
                    if grid[r][c] == WALL or grid[r][c] == GUARD:
                        break
                    if grid[r][c] == 0:
                        grid[r][c] = GUARDED
                    r += dr
                    c += dc
        
        unguarded = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    unguarded += 1
        
        return unguarded
