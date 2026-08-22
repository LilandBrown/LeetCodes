class Solution(object):
    #incomplete
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def recGenerateParanthesis(n):
            if (n == 1):
                return ["()"]
            else:
                subList = recGenerateParanthesis(n - 1)
                retList = []
                for i in subList:
                    if i + "()" == "()" + i:
                        retList.append(i  + "()")
                    else:
                        retList.append(i  + "()")
                        retList.append("()" + i)
                    retList.append("()" + i + "")
        return recGenerateParanthesis(n)
