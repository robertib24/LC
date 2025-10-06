class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        
        heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        
        while heap:
            time, x, y = heapq.heappop(heap)
            
            if x == n-1 and y == n-1:
                return time
            
            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    new_time = max(time, grid[nx][ny])
                    heapq.heappush(heap, (new_time, nx, ny))
        
        return -1
