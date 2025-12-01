class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def canRun(k):
            total = 0
            for battery in batteries:
                total += min(battery, k)
            return total >= n * k
        
        left, right = 0, sum(batteries) // n
        result = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canRun(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result
