class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        js = nums[0]
        index = 1
        length = len(nums)
        while js > 0 and index < length:
            js -= 1
            js = max(js, nums[index])
            index += 1
        if index == length:
            return True
        if js == 0:
            return False
        