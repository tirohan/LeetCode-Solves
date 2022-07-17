class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """

        :type s: str

        :type numRows: int

        :rtype: str

        """

        if numRows == 1:

            return s

        zigzag = [[] for _ in range(numRows)]

        row = 0

        direction = -1      # -1 for up, +1 for down

        for c in s:

            zigzag[row].append(c)

            if row == 0 or row == numRows-1:    # change direction

                direction = -direction

            row += direction
