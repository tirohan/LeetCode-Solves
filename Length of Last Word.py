class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        preLength = 0   # Length of previous word
        length = 0      # Length of current word
        for letter in s:
            if letter == " ":           # Waiting for the next word
                if length != 0:         # This is a single zero or
                                        # leading one in zeros
                    preLength = length
                    length = 0
                else:                   # A following zero in zeros
                    pass
            else:
                # Inside one word
                length += 1
        if length == 0:
            return preLength    # s ends with zero(s)
        else:
            return length