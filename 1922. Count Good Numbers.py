class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        def pow(x, n):
            res = 1
            while n:
                if n % 2:
                    res = (res * x)
                n //= 2
                x = (x * x) % MOD

            return res

        even = ceil(n / 2)
        odd = n // 2

        return (pow(5, even) * pow(4, odd)) % MOD
