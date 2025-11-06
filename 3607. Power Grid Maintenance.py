class Solution:
    def processQueries(self, c: int, connections: list[list[int]], queries: list[list[int]]) -> list[int]:
        
        adj = defaultdict(list)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        component_id = [-1] * (c + 1)
        component_data = []
        current_comp_id = 0
        
        for i in range(1, c + 1):
            if component_id[i] == -1:
                component_data.append(SortedList())
                q = deque([i])
                component_id[i] = current_comp_id
                component_data[current_comp_id].add(i)
                
                while q:
                    u = q.popleft()
                    for v in adj[u]:
                        if component_id[v] == -1:
                            component_id[v] = current_comp_id
                            component_data[current_comp_id].add(v)
                            q.append(v)
                current_comp_id += 1
        
        online = [True] * (c + 1)
        results = []
        
        for query_type, x in queries:
            if query_type == 2:
                if online[x]:
                    online[x] = False
                    comp_id = component_id[x]
                    component_data[comp_id].remove(x)
            else:
                if online[x]:
                    results.append(x)
                else:
                    comp_id = component_id[x]
                    if component_data[comp_id]:
                        results.append(component_data[comp_id][0])
                    else:
                        results.append(-1)
                        
        return results
