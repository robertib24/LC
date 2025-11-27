class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        f = [float('inf')] * k
        ans = float('-inf')
        s = 0
        f[k - 1] = 0
        
        for i, x in enumerate(nums):
            s += x
            ans = max(ans, s - f[i % k])
            f[i % k] = min(f[i % k], s)
        
        return ans
