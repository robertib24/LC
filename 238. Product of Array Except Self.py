# Bruteforce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = nums^2 * len(list)

        for i in range(len(nums)):
            prod = 1
            for j in range(len(nums)):
                if i == j:
                    continue    
                prod *= nums[j]
            
            res[i] = prod
        return res

# O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        post = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res
