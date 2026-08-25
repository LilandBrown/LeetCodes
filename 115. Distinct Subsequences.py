class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        arr = [0] * (len(t)+ 1)
        arr [0] = 1
        for i in s:
            for j in range(len(t), 0, -1):
                if i == t[j - 1]:
                    arr [j] += arr [j - 1]
        return arr [len(t)]    