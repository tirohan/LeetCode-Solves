class Solution:
    def makeGood(self, s: str) -> str:
        #main subroutine
        stk = []
        for ch in s:
            counter_ch = ch.upper() if ch.islower() else ch.lower()
            if stk and stk[-1] == counter_ch:
                stk.pop()
            else:
                stk.append(ch)
        return "".join(stk)
