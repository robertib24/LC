class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        if k == 1:
            return n >= 2
        
        inc_len = [1] * n
        
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc_len[i] = inc_len[i - 1] + 1
            else:
                inc_len[i] = 1
        
        for i in range(k - 1, n - k):
            if inc_len[i] >= k and inc_len[i + k] >= k:
                return True
        
        return False
