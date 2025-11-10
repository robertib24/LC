class Solution:
    def minOperations(self, nums: list[int]) -> int:
        stack = [-1]
        operations = 0
        
        for num in nums:
            while stack and stack[-1] > num:
                stack.pop()
            
            if num > stack[-1]:
                if num > 0:
                    operations += 1
                stack.append(num)
        
        return operations
