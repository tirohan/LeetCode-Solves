class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """

        :type intervals: List[List[int]]

        :type newInterval: List[int]

        :rtype: List[List[int]]
s
        """

        left, right = 0, len(intervals) - 1

        while left < len(intervals) and intervals[left][1] < newInterval[0]:

            left += 1

        while right >= 0 and intervals[right][0] > newInterval[1]:

            right -= 1

        if left <= right:

            newInterval[0] = min(newInterval[0], intervals[left][0])

            newInterval[1] = max(newInterval[1], intervals[right][1])

        return intervals[:left] + [newInterval] + intervals[right + 1:]