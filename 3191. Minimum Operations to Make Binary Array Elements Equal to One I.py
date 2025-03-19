class Solution:
    def flip(self, nums, pos):
        nums[pos] ^= 1
        nums[pos + 1] ^= 1
        nums[pos + 2] ^= 1

    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ops = 0

        for i in range(n-2):
            if nums[i] == 1:
                continue
            self.flip(nums, i)
            ops += 1

        if nums[n-1] == 0 or nums[n-2] == 0:
            return -1
        
        return ops
        
