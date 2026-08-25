class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        maxi = int(len(nums) > 0)
        for i in s:
            if i-1 not in s:
                j = 1
                while i + j in s:
                    j += 1
                    maxi = max(j, maxi)
        return maxi