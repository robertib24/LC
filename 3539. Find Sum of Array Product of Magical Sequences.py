class Solution:
    def magicalSum(self, m: int, k: int, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        def getComb(n, k):
            comb = [[0] * (k + 1) for _ in range(n + 1)]
            for i in range(n + 1):
                comb[i][0] = 1
            for i in range(1, n + 1):
                for j in range(1, min(i, k) + 1):
                    comb[i][j] = (comb[i-1][j] + comb[i-1][j-1]) % MOD
            return comb
        
        def modPow(x, n):
            if n == 0:
                return 1
            if n % 2 == 1:
                return (x * modPow(x, n - 1)) % MOD
            half = modPow(x, n // 2)
            return (half * half) % MOD
        
        comb = getComb(m, m)
        memo = {}
        
        def dp(remaining_m, remaining_k, idx, carry):
            if remaining_m < 0 or remaining_k < 0:
                return 0
            if remaining_m + bin(carry).count('1') < remaining_k:
                return 0
            if remaining_m == 0:
                return 1 if bin(carry).count('1') == remaining_k else 0
            if idx == n:
                return 0
            
            state = (remaining_m, remaining_k, idx, carry)
            if state in memo:
                return memo[state]
            
            res = 0
            for count in range(remaining_m + 1):
                contribution = (comb[remaining_m][count] * modPow(nums[idx], count)) % MOD
                new_carry = carry + count
                res = (res + dp(remaining_m - count, remaining_k - (new_carry % 2), 
                               idx + 1, new_carry // 2) * contribution) % MOD
            
            memo[state] = res
            return res
        
        return dp(m, k, 0, 0)
