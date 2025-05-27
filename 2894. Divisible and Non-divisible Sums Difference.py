class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        div = []
        nondiv = []

        for x in range(1, n + 1):
            if x % m == 0:
                div.append(x)
            else:
                nondiv.append(x)

        return sum(nondiv) - sum(div)g
