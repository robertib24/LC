class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        
        valid_count = 0
        left_sum = 0
        
        for num in nums:
            if num != 0:
                left_sum += num
            else:
                if left_sum * 2 == total_sum:
                    valid_count += 2
                elif abs(left_sum * 2 - total_sum) == 1:
                    valid_count += 1
        
        return valid_count
