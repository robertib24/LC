class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        arr = sorted(x + y for x,y in pairwise(weights))
        return sum(arr[len(arr) - k + 1 :]) - sum(arr[: k - 1])
