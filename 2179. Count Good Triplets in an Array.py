class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)

        mapping = [None] * N
        for index, x in enumerate(nums1):
            mapping[x] = index

        mnums2 = []
        for x in nums2:
            mnums2.append(mapping[x])

        seen = SortedList()

        total = 0

        for x in mnums2:
            left = len(seen)
            smaller_left = seen.bisect_left(x)

            right = N - 1 - left
            bigger = N - 1 - x
            bigger_left = left - smaller_left
            bigger_right = bigger - bigger_left

            total += smaller_left * bigger_right

            seen.add(x)
        
        return total

        
