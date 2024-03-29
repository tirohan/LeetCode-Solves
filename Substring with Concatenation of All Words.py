class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """

        :type s: str

        :type words: List[str]

        :rtype: List[int]

        """

        result = []

        word_len = len(words[0])

        for stripe in range(word_len):  # each stripe starts at a different position in s, modulo word_len

            i = stripe                  # the next index in s that we want to match a word

            to_match = len(words)       # number of words still to be matched

            freq = Counter(words)       # frequency of each words to be matched

            while i + to_match*word_len <= len(s):  # remainder of s is long enough to hold remaining unmatched words

                word = s[i:i+word_len]   # next part of s attempting to be matched

                if word in freq:         # match, decrement freq count

                    freq[word] -= 1

                    if freq[word] == 0:

                        del freq[word]

                    to_match -= 1

                    i += word_len

                    if to_match == 0:               # all matched

                        result.append(i - word_len*len(words))

                elif to_match != len(words):        # some words have been matched

                    nb_matches = len(words) - to_match

                    first_word = s[i - nb_matches*word_len:i - (nb_matches-1)*word_len]

                    freq.setdefault(first_word, 0)  # put first word matched back in dictionary

                    freq[first_word] += 1

                    to_match += 1

                else:                               # no words matched

                    i += word_len

        return result