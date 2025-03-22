class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = {i:[] for i in range(n)}
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(count, node) -> bool :
            ans = 1 
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    if len(graph[n]) != count:
                        ans = 0
                    ans = min(ans, dfs(count, n))
            return ans

        ans = 0
        for i in range(n):
            if i not in visited:
                pre = len(visited)
                visited.add(i)
                if dfs(len(graph[i]), i) and len(graph[i]) == (len(visited) - pre) - 1:
                    ans += 1
                
        return ans
