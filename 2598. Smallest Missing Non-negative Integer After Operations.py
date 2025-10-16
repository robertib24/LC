class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        count = {}
        for num in nums:
            rest = num % value
            count[rest] = count.get(rest, 0) + 1
        
        answer = 0
        while count.get(answer % value, 0) > 0:
            count[answer % value] -= 1
            answer += 1
        
        return answer
