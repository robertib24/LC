class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        remaining_days = n % 7
        
        complete_weeks_sum = weeks * 28 + 7 * weeks * (weeks - 1) // 2
        
        remaining_sum = (weeks * 2 + remaining_days + 1) * remaining_days // 2
        
        return complete_weeks_sum + remaining_sum
