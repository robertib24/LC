class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_len = start_index = mask = 0

        for end_index, num in enumerate(nums):

            while mask & num:
                mask ^= nums[start_index]
                start_index += 1

            max_len = max(max_len, end_index - start_index + 1)
            mask |= num

        return max_len  


            
        
