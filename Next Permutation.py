class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """

        :type nums: List[int]

        :rtype: void Do not return anything, modify nums in-place instead.

        """

        if not nums or len(nums) == 1:

            return

        i = len(nums)-2     # starting at back, find the first decrease - increasing it will increment the permutation

        while i >= 0 and nums[i] >= nums[i+1]:

            i -= 1

        if i != -1:         # if any decrease then find the smallest larger number to swap with

            j = i+1

            while j < len(nums) and nums[j] > nums[i]:

                j += 1

            j -= 1

            nums[i], nums[j] = nums[j], nums[i]

        # reverse all from i+1 onwards since they were decreasing and increasing minimises permutation

        left = i+1

        right = len(nums)-1

        while left < right:

            nums[left], nums[right] = nums[right], nums[left]

            left += 1

            right -= 1