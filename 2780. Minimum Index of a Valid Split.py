class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        x, cnt = Counter(nums).most_common(1)[0]
        curr = 0
        for i, v in enumerate(nums, 1):
            if v == x:
                curr += 1
                if curr * 2 > i and (cnt - curr) * 2 > len(nums) - i:
                    return i - 1
        return -1
