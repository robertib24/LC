class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, float('-inf'), float('-inf')]
        
        for num in nums:
            temp = dp[:]
            for i in range(3):
                new_mod = (i + num) % 3
                temp[new_mod] = max(temp[new_mod], dp[i] + num)
            dp = temp
        
        return dp[0]
