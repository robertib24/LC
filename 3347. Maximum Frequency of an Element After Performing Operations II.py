class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        cnt = {}
        d = {}
        
        for x in nums:
            cnt[x] = cnt.get(x, 0) + 1
            d[x] = d.get(x, 0)
            d[x - k] = d.get(x - k, 0) + 1
            d[x + k + 1] = d.get(x + k + 1, 0) - 1
        
        ans = 0
        s = 0
        
        for x in sorted(d.keys()):
            s += d[x]
            ans = max(ans, min(s, cnt.get(x, 0) + numOperations))
        
        return ans
