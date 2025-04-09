class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sett = set()
        for num in nums:
            if num < k:
                return -1
            elif num > k:
                sett.add(num)
        
        return len(sett)
        
