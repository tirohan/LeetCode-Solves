class Solution:
    def reverse(self, x: int) -> int:
        """

        :type x: int

        :rtype: int

        """

        negative = x < 0    # record if negative and change to positive

        x = abs(x)

        reversed = 0

        while x != 0:

            reversed = reversed * 10 + x % 10

            x //= 10

        if reversed > 2**31 - 1:    # required to pass leetcode test cases, not applicable for python

            return 0

        return reversed if not negative else -reversed