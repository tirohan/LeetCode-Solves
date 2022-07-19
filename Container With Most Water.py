class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        max_area = (right - left) * min(height[right], height[left])

        while left < right:
            if height[left] < height[right]:    # By moving in the lower boundary we have the possibility
                left += 1                       # of finding a larger area.
            else:
                right -= 1
            max_area = max(max_area, (right - left) * min(height[right], height[left]))

        return max_area