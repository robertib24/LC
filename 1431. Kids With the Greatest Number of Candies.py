class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        ans=[]
        for i in range(len(candies)):
            ans.append(candies[i] + extraCandies >= max(candies))
        return ans
