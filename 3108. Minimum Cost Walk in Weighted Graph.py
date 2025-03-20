class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        self.par = [ i for i in range(n) ]
        self.rank = [ 1 for _ in range(n) ]
        self.cost = [-1] * n

        def update_cost(nd, prev, w):
            if self.cost[nd] == -1:
                self.cost[nd] = w
            else:
                self.cost[nd] = self.cost[nd] & self.cost[prev] & w
            

        def find(node):
            if node == self.par[node]:
                return node
            return find(self.par[node])

        def union(n1, n2, w):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                update_cost(p1, p1, w)
                return
            
            if self.rank[p2] > self.rank[p1]:
                self.par[p1] = p2
                self.rank[p2] += self.rank[p1]
                update_cost(p2, p1, w)
            else:
                self.par[p2] = p1
                self.rank[p1] += self.rank[p2]
                update_cost(p1, p2, w)

        for n1, n2, w in edges:
            union(n1, n2, w)
        
        res = []
        
        for u, z in query:
            p1, p2 = find(u), find(z)
            if p1 == p2:
                res.append(self.cost[p1])
            else:
                res.append(-1)
        
        return res

