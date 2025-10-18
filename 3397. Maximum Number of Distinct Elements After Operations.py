class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        ans = 0
        pre = float('-inf')

        for x in nums:
            curr = min(x + k, max(x - k, pre + 1))
            if curr > pre:
                ans += 1
                pre = curr

        return ans

        
