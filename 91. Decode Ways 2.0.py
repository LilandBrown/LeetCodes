class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def isValid(msg):
                    if (msg[0] == "0"):
                        return False
                    if (int(msg) > 0 and int(msg) < 27):
                        return True
                    return False

        arrTotal = [0] * len(s)

        if isValid(s[len(s) - 1 : len(s)]):
            arrTotal [len(s) - 1] = 1

        if (len(s) == 1):
            return arrTotal[0]
            
        if isValid(s[len(s) - 2 : len(s)]):
            arrTotal [len(s) - 2] += 1
        
        if isValid(s[len(s) - 2 : len(s) - 1]):
            arrTotal  [len(s) - 2] += arrTotal [len(s) - 1]

        for i in range(len(s) - 3, -1, -1): 

            if isValid(s[i : i + 2]):
                arrTotal[i] += arrTotal[i + 2]
            
            if isValid(s[i : i + 1]):
                arrTotal[i] += arrTotal[i + 1]

        return arrTotal[0]