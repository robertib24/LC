class Solution:
    def maximumTotalDamage(self, power):
        if not power:
            return 0
        
        power.sort()
        
        unique = []
        counts = []
        i = 0
        while i < len(power):
            val = power[i]
            count = 0
            while i < len(power) and power[i] == val:
                count += 1
                i += 1
            unique.append(val)
            counts.append(count)
        
        n = len(unique)
        if n == 0:
            return 0
        if n == 1:
            return unique[0] * counts[0]
        
        dp = [0] * n
        dp[0] = unique[0] * counts[0]
        
        for i in range(1, n):
            skip = dp[i - 1]
            
            take = unique[i] * counts[i]
            j = i - 1
            while j >= 0 and unique[j] >= unique[i] - 2:
                j -= 1
            if j >= 0:
                take += dp[j]
            
            dp[i] = max(skip, take)
        
        return dp[n - 1]
