class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def count():
            res, prev_end = 0,-1
            for start, end in points:
                if start>=prev_end:
                    res += 1
                    if res == 3: return True
                prev_end = max(prev_end,end)
            return False
            
        points = []

        for x1,_,x2,_ in rectangles: points.append((x1,x2))
        points.sort()   
        if count(): return True

        points.clear()

        for _,y1,_,y2 in rectangles: points.append((y1,y2))
        points.sort() 
        if count(): return True

        return False
        
