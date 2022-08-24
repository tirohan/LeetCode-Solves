class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """

        :type n: int

        :rtype: List[str]

        """

        result = []

        self.generate([], n, n, result)

        return result

    # Generates all parentheses given a starting prefix and remaining left and right brackets.

    def generate(self, prefix, left, right, result):

        if left == 0 and right == 0:

            result.append("".join(prefix))

        if left != 0:

            self.generate(prefix + ['('], left-1, right, result)

        if right > left:

            self.generate(prefix + [')'], left, right-1, result)
