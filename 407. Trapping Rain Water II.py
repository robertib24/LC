class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        if not heightMap or not heightMap[0]:
            return 0

        m = len(heightMap)
        n = len(heightMap[0])

        if m < 3 or n < 3:
            return 0

        heap = []
        visited = set()

        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i, j))

        water = 0
        max_height = 0

        while heap:
            h, i, j = heapq.heappop(heap)
            max_height = max(max_height, h)

            for di, dj in [(0,1), (0,-1), (1, 0), (-1, 0)]:
                ni = i + di
                nj = j + dj

                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    visited.add((ni, nj))

                    if heightMap[ni][nj] < max_height:
                        water += max_height - heightMap[ni][nj]
                    
                    heapq.heappush(heap, (heightMap[ni][nj], ni, nj))

        return water
