class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False

        target = s // 2
        n = len(nums)
        dp = [[-1 for _ in range(target + 1)] for _ in range(n)]

        def subset(s, i):
            if s == 0:
                return True
            if i < 0:
                return False
            if dp[i][s] != -1:
                return dp[i][s]
            if nums[i] <= s:
                dp[i][s] = subset(s - nums[i], i - 1) or subset(s, i - 1)
            else:
                dp[i][s] = subset(s, i - 1)
            return dp[i][s]

        return subset(target, n - 1)
