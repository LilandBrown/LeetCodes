class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        arr = False * len(s)
        for i in range (len(s)):
            for j in range(max(i, 20)):
                if (arr [i - j] == True and s[i-j :i] in wordDict):
                    arr [i] = True
        return arr [len(s)]