from functools import cache

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        n = len(s)

        def count_up_to(x: int) -> int:
            t = str(x)

            @cache
            def dfs(pos: int, tight: bool) -> int:
                if len(t) < n:
                    return 0
                if len(t) - pos == n:
                    return int(t[pos:] >= s) if tight else 1

                upper_bound = min(int(t[pos]) if tight else 9, limit)
                total = 0
                for digit in range(upper_bound + 1):
                    total += dfs(pos + 1, tight and digit == int(t[pos]))
                return total

            return dfs(0, True)

        return count_up_to(finish) - count_up_to(start - 1)
