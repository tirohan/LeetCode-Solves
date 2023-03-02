class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompressed = []
        
        for i in range(0, len(nums)-1, 2):
            decompressed = decompressed + nums[i] * [nums[i+1]]
    
        return decompressed