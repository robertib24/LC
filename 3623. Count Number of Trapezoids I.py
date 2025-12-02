class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        y_counts = {}
        for x, y in points:
            y_counts[y] = y_counts.get(y, 0) + 1
        
        y_values = sorted(y_counts.keys())
        
        edge_counts = []
        for y in y_values:
            n = y_counts[y]
            edge_counts.append((n * (n - 1) // 2) % MOD)
        
        result = 0
        prefix_sum = 0
        
        for count in edge_counts:
            result = (result + count * prefix_sum) % MOD
            prefix_sum = (prefix_sum + count) % MOD
        
        return result
