class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def twoSum(self, numbers, target):
                """
                :type numbers: List[int]
                :type target: int
                :rtype: List[int]
                """
                l = 0
                r = len(numbers) - 1
                while numbers[l] + numbers[r] != target:
                    if numbers[l] + numbers[r] > target:
                        r -= 1
                    else:
                        l += 1
                return [l+1, r+1]
        num = sorted(set(nums))
        