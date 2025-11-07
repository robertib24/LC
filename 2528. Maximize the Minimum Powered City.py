class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        power = [0] * n
        
        window_sum = sum(stations[:min(n, r + 1)])
        power[0] = window_sum
        
        for i in range(1, n):
            if i + r < n:
                window_sum += stations[i + r]
            if i - r - 1 >= 0:
                window_sum -= stations[i - r - 1]
            power[i] = window_sum
        
        def canAchieve(minPower):
            add = stations[:]
            used = 0
            window_sum = sum(add[:min(n, r + 1)])
            
            for i in range(n):
                if i > 0:
                    if i + r < n:
                        window_sum += add[i + r]
                    if i - r - 1 >= 0:
                        window_sum -= add[i - r - 1]
                
                if window_sum < minPower:
                    need = minPower - window_sum
                    used += need
                    if used > k:
                        return False
                    pos = min(n - 1, i + r)
                    add[pos] += need
                    window_sum += need
            
            return True
        
        left, right = min(power), sum(stations) + k
        result = left
        
        while left <= right:
            mid = (left + right) // 2
            if canAchieve(mid):
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return result
