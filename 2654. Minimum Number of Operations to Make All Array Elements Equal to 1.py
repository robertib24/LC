class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        ones = nums.count(1)
        if ones > 0:
            return n - ones
        
        overall_gcd = nums[0]
        for num in nums:
            overall_gcd = gcd(overall_gcd, num)
        
        if overall_gcd > 1:
            return -1
        
        min_ops = float('inf')
        
        for i in range(n):
            current_gcd = nums[i]
            for j in range(i + 1, n):
                current_gcd = gcd(current_gcd, nums[j])
                if current_gcd == 1:
                    min_ops = min(min_ops, j - i)
                    break
        
        return min_ops + n - 1
