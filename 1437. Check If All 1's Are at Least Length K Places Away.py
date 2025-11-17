class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -float('inf')
        
        for i in range(len(nums)):
            if nums[i] == 1:
                if i - prev - 1 < k:
                    return False
                prev = i
        
        return True
