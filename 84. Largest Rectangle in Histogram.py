class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        s = []
        s.append([0, heights[0]])
        r = 0
        l = len(heights)
        for i in range(1, len(heights)):
            if s[-1][1] < heights[i]:
                s.append([i, heights[i]])
            else:
                left = i
                while s and s[-1][1] > heights[i]:
                    top = s.pop()
                    if r < top[1] * (i - top[0]):
                        r = top[1] * (i - top[0])
                    left = top[0]
                s.append([left, heights[i]])
        while s:
            top = s.pop()
            if r < top[1] * (l - top[0]):
                r = top[1] * (l - top[0])
        return r