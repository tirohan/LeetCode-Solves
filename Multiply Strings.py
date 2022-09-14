class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """

        :type num1: str

        :type num2: str

        :rtype: str

        """

        num1, num2 = num1[::-1], num2[::-1]         # easier to work with lowest digits first

        result = [0] * (len(num1) + len(num2))

        for i in range(len(num1)):

            int1 = ord(num1[i]) - ord('0')

            for j in range(len(num2)):

                int2 = ord(num2[j]) - ord('0')

                tens, units = divmod(int1 * int2, 10)

                result[i + j] += units      # add units and handle carry of units

                if result[i + j] > 9:

                    result[i + j + 1] += result[i + j] // 10

                    result[i + j] %= 10

                result[i + j + 1] += tens   # add tens and handle carry of tens

                if result[i + j + 1] > 9:

                    result[i + j + 2] += result[i + j + 1] // 10

                    result[i + j + 1] %= 10

        while len(result) > 1 and result[-1] == 0:  # remove trailing zeros

            result.pop()

        return "".join(map(str, result[::-1]))      # reverse and convert to string