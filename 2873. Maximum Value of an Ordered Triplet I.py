class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        left = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > left:
                left = nums[i]
                continue
            for j in range(i + 1, len(nums)):
                ans = max(ans, (left - nums[i]) * nums[j])
            
        return ans
        
