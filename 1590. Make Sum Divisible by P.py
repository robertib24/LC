class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p
        
        if target == 0:
            return 0
        
        mod_map = {0: -1}
        curr_sum = 0
        min_len = len(nums)
        
        for i, num in enumerate(nums):
            curr_sum = (curr_sum + num) % p
            needed = (curr_sum - target + p) % p
            
            if needed in mod_map:
                min_len = min(min_len, i - mod_map[needed])
            
            mod_map[curr_sum] = i
        
        return min_len if min_len < len(nums) else -1
