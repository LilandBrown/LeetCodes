class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        possible = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        possible [0] [0] = True
        if (len(s1) + len(s2) != len(s3)):
            return False
        for i in range (1, len(s1) + 1):
            if possible [i - 1] [0] and s1[i - 1] == s3[i - 1]:
                possible [i] [0] = True
            else:
                 possible [i] [0] = False
        for i in range (1, len(s2) + 1):
            if possible [0] [i - 1]  and s2[i - 1] == s3[i - 1]:
                possible [0] [i] = True
            else:
                possible [0] [i] = False
        for i in range (1, len(s1) + 1):
            for j in range (1, len(s2) + 1):
                if possible [i] [j - 1] and s2[j - 1] == s3[i + j - 1] or possible [i - 1] [j] and s1[i - 1] == s3[i + j - 1]:
                    possible [i] [j] = True
                else:
                    possible [i] [j] = False
        return possible [len(s1)] [len(s2)]
                    