class Solution(object):
    def setZeroes(self, matrix):
        if not matrix:
            return
        l = len(matrix)
        w = len(matrix[0])
        x_zeros = set()
        y_zeros = set()
        for i in range(l):
            for j in range(w):
                if matrix[i][j] == 0:
                    x_zeros.add(j)
                    y_zeros.add(i)

        for i in y_zeros:
            matrix[i] = [0] * w
        for i in x_zeros:
            for j in range(l):
                matrix[j][i] = 0
