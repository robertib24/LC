class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        dp = [[[0] * k for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] = 1
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                for r in range(k):
                    if i > 0:
                        prev_r = (r - grid[i][j]) % k
                        dp[i][j][r] = (dp[i][j][r] + dp[i-1][j][prev_r]) % MOD
                    if j > 0:
                        prev_r = (r - grid[i][j]) % k
                        dp[i][j][r] = (dp[i][j][r] + dp[i][j-1][prev_r]) % MOD
        
        return dp[m-1][n-1][0]
