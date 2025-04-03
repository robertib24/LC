class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        max_diff = 0
        left = nums[0]
        for i in range(1, len(nums)):
            ans = max(ans, max_diff * nums[i])
            left = max(left, nums[i])
            max_diff = max(max_diff, left - nums[i])
        return ans
        
