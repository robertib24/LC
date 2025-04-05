class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        rez = 0
        for num in nums:
            rez = rez | num
        
        return rez << (len(nums) - 1)

        
