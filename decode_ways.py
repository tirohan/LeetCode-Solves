class Solution:
    def numDecodings(self, s: str) -> int:
        size = len(s)
        if size == 0 or s[0] == '0':
            return 0
        dp = [1, 1]
        for i in range(1, size):
            curWays = 0
            if s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                curWays += dp[-2]
            if s[i] != '0':
                curWays += dp[-1]
            if curWays == 0:
                return 0
            dp.append(curWays)
        return dp[-1]