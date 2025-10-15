class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        ans = 0
        pre = 0
        curr = 0

        for i, x in enumerate(nums):
            curr += 1

            if i == len(nums) - 1 or x >= nums[i + 1]:
                ans = max(ans, curr // 2, min(pre, curr))
                pre = curr
                curr = 0

        return ans
