class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr =  [1] * len(nums)
        l = 1
        r = 1
        
        for i in range(len(nums)):
            te = nums[i]
            arr [i] *= l
            l *= te
        
        for i in range(len(nums) -1 , -1, -1):
            te = nums[i]
            arr [i] *= r
            r *= te
        return arr
        