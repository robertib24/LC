class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        ans = 0
        mx = -1
        second_max = -1
        
        for start, end in intervals:
            if mx >= start and second_max >= start:
                continue
            
            if mx >= start:
                second_max = mx
                mx = end
                ans += 1
            else:
                mx = end
                second_max = end - 1
                ans += 2
        
        return ans
