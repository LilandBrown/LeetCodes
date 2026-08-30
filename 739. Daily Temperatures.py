class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        rL = [0] * len(temperatures)
        s = []
        for i, ch in enumerate(temperatures):
            while(s and ch > s[-1][0]):
                    top = s.pop()
                    rL[top[1]] = i - top[1]
            s.append([ch, i])
        return rL