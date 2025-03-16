class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # n = sqrt(t/r)

        l = 1
        r = 10**14

        def fun(target):
            reparat = 0
            for r in ranks:
                reparat += int(sqrt(target/r))
            return reparat >= cars

        while l < r:
            mid = (l + r) // 2
            
            if fun(mid):
                r = mid
            else:
                l = mid + 1
        return l 
        
