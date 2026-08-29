class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        l = 0
        mx = 0
        for i in range(len(s)):
            if s[i] in d:
                l = max(l, d[s[i]] + 1)
                d[s[i]] = i
            else:
                d[s[i]] = i
            mx = max(mx, i - l)
        if len(s) == 0:
            return 0
        return mx + 1