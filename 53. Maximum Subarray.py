class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls = nums[0]
        cs= 0
        for i in nums:
            cs += i
            if cs > ls:
                ls = cs
            if cs < 0:
                cs = 0
        return ls