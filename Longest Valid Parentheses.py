class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """

        :type s: str

        :rtype: int

        """

        stack = []                  # indices of brackets that are not matched

        for i, c in enumerate(s):

            if c == ")" and stack and s[stack[-1]] == '(':

                stack.pop()         # close matches an open on the stack

            else:

                stack.append(i)     # puch open brackets or unmatched close brackets

        stack.append(len(s))        # last unmatched index after end of s

        max_length = stack[0]       # first unmatched index before start of s

        for index in range(1, len(stack)):  # find max gap between remaining unmatched indices

            max_length = max(max_length, stack[index] - stack[index-1] - 1)

        return max_length