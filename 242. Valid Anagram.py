class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d = {} 
        for i in s:
            if i in d:
                d[i] = d[i] + 1
            else:
                d[i] = 1
        for i in t:
            if i not in d:
                return False
            elif d[i] > 1:
                d[i] = d[i] - 1
            else:
                del d[i]
        return len(d) == 0