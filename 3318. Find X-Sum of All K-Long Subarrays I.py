class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        ans = []
        
        for i in range(len(nums) - k + 1):
            window = nums[i:i + k]
            
            freq = {}
            for num in window:
                freq[num] = freq.get(num, 0) + 1
            
            items = [(count, num) for num, count in freq.items()]
            items.sort(reverse=True)
            
            xsum = 0
            for j in range(min(x, len(items))):
                count, num = items[j]
                xsum += count * num
            
            ans.append(xsum)
        
        return ans
