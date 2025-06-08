class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        temp = [str(i) for i in range(1, n + 1)]
        temp.sort()
        temp = [int(i) for i in temp]
        return temp
