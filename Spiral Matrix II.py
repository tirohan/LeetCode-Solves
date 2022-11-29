class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for i in range(n):
            matrix.append([0] * n)
        val = 1
        num = 0
        while num <= n // 2:
            for i in range(num, n - num):
                if matrix[num][i] == 0:
                    matrix[num][i] = val
                    val += 1
            for i in range(num, n - num):
                if matrix[i][n - num - 1] == 0:
                    matrix[i][n - num - 1] = val
                    val += 1
            for i in range(n - num - 1, num - 1, -1):
                if matrix[n - num - 1][i] == 0:
                    matrix[n - num - 1][i] = val
                    val += 1
            for i in range(n - num - 1, num - 1, -1):
                if matrix[i][num] == 0:
                    matrix[i][num] = val
                    val += 1
            num += 1
        return matrix