class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """

        :type matrix: List[List[int]]

        :rtype: void Do not return anything, modify matrix in-place instead.

        """

        n = len(matrix)

        layers = n//2

        for layer in range(layers):

            for i in range(layer, n - layer - 1):

                temp = matrix[layer][i]

                matrix[layer][i] = matrix[n - 1 - i][layer]

                matrix[n - 1 - i][layer] = matrix[n - 1 - layer][n - 1- i]

                matrix[n - 1 - layer][n - 1 - i] = matrix[i][n - 1 - layer]

                matrix[i][n - 1 - layer] = temp