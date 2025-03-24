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
        
