class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        output = 0
        for i in range(len(height)):
            filled = 0
            while stack and stack[-1] [0] <= height[i]:
                top = stack.pop()
                output += (top[0] - filled) * (i - top[1] - 1)
                filled = top[0]
            if stack:
                output += (height[i] - filled) * (i - stack[-1][1] - 1)
            stack.append([height[i], i])
        return output