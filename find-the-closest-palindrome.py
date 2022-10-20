class Solution:
      def nearestPalindromic(self, n: str) -> str:
        prefix = int(n[:(len(n)+1)//2])
            
        candidates = set(['1' + '0' * (len(n)-1) + '1', '9' * (len(n)-1)]) 
        
        for i in map(str, [prefix-1, prefix, prefix+1]):                  
            candidates.add(i + [i, i[:-1]][len(n) & 1][::-1])
            
        candidates.discard(n)                                              
        candidates.discard('')                                            
        
        return min(candidates, key = lambda x: (abs(int(x) - int(n)), int(x)))