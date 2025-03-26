class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:

        left = 0
        right = 10**10
        ans = -1

        med = 0
        temp = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp.append(grid[i][j])
        temp.sort()

        n = len(grid) * len(grid[0])
        med = temp[n//2]

        def good(mid):
            opr = 0
            for i in range(len(grid)):
                for j in range(len(grid[i])):
                    tgt = abs(med - grid[i][j])
                    if tgt % x != 0:
                        return False
                    opr += tgt // x
                    if opr > mid:
                        return False
            return True


        while left <= right:
            mid = (left + right) // 2
            if good(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

