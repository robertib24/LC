class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consec = 3
        for num in arr:
            if num % 2:
                consec -= 1
            else:
                consec = 3
            if consec == 0:
                return True
        return False
