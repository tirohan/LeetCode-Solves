class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_len = 0
        # 
        last_idx = {}
        # starting index of current window to calculate max_len
        start_idx = 0

        for i in range(0, len(s)):
            if s[i] in last_idx:
                start_idx = max(start_idx, last_idx[s[i]] + 1)
            # Update result if we get a larger window
            max_len = max(max_len, i-start_idx + 1)
            # Update last index of current char.
            last_idx[s[i]] = i
        return max_len
