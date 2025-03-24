class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        merged = []

        for i in meetings:
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], i[1])]

        unavailable_days = 0

        for start,end in merged:
            unavailable_days += end - start + 1

        return days - unavailable_days

# 2nd sol
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        meetings.sort()
        p_end = 0

        for start, end in meetings:
            start = max(start, p_end + 1)
            length = end - start + 1
            days -= max(length, 0)
            p_end = max(end, p_end)
            
        return days 
        
        
