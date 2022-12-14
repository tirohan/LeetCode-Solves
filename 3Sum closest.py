class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        
        result = nums[0] + nums[1] + nums[len(nums) - 1]
        
        for i in range(len(nums) - 1):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current = nums[i] + nums[left] + nums[right]
                
                if current == target:
                    return target
                
                elif abs(target - current) < abs(target - result):
                    result = current 
                
                elif current > target:
                    right = right - 1
                    
                else:
                    left = left + 1
                    
        return result 