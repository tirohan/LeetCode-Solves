class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """

        :type n: int

        :type k: int

        :rtype: str

        """

        chars = [str(i) for i in range(1, n+1)]     # the symbols that will be permuted

        permutations = factorial(n)                 # total number of permutations for this n

        k -= 1                                      # change indexing to 0

        result = []

        while chars:

            digit = n * k // permutations           # get the first digit (range is 0 to n-1)

            result.append(chars[digit])             # map from digit to a symbol

            del chars[digit]                        # remove that symbol

            permutations //= n                      # repeat for next digit with decreased permutations, n and k

            k -= digit * permutations

            n -= 1

        return "".join(result)