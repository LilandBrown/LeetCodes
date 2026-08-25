class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for i in range(len(strs)):
            st = "".join(sorted(strs[i])) 
            if st in d:
                d[st].append(i)
            else:
                d[st] = [i]
        ret = []
        for i in d:
            r1 = []
            for j in d[i]:
                r1.append(strs[j])
            ret.append(r1)
        return ret