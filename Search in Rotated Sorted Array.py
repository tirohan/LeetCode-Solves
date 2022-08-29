class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

        :type nums: List[int]

        :type target: int

        :rtype: int

        """

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:

                return mid

            if nums[left] <= nums[mid]:  # LHS is sorted

                if target >= nums[left] and target < nums[mid]:  # target is on LHS

                    right = mid - 1

                else:

                    left = mid + 1

            else:  # RHS is sorted

                if target <= nums[right] and target > nums[mid]:  # target is on RHS

                    left = mid + 1

                else:

                    right = mid - 1

        return -1