class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        hashMap_A = {}
        hashMap_B = {}

        for index, x in enumerate(pattern):
            if x not in hashMap_A:
                hashMap_A[x] = [index]
            else:
                hashMap_A[x].append(index)

        for index, x in enumerate(s.split()):
            if x not in hashMap_B:
                hashMap_B[x] = [index]
            else:
                hashMap_B[x].append(index)

        return list(hashMap_A.values()) == list(hashMap_B.values())