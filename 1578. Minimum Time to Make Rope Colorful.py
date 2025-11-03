class Solution:
    def minCost(self, colors: str, neededTime: list[int]) -> int:
        total_cost = 0
        i = 0
        n = len(colors)
        
        while i < n:
            j = i
            total_group_cost = 0
            max_cost = 0
            
            while j < n and colors[j] == colors[i]:
                total_group_cost += neededTime[j]
                max_cost = max(max_cost, neededTime[j])
                j += 1
            
            if j - i > 1:
                total_cost += total_group_cost - max_cost

            i = j    
            
        return total_cost
