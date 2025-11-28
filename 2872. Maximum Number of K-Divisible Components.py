class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        self.ans = 0
        
        def dfs(node, parent):
            subtree_sum = values[node]
            for neighbor in graph[node]:
                if neighbor != parent:
                    subtree_sum += dfs(neighbor, node)
            
            if subtree_sum % k == 0:
                self.ans += 1
            
            return subtree_sum
        
        dfs(0, -1)
        return self.ans
