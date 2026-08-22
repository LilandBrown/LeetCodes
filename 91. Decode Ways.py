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
        def recNumDecoding(msg):
            if (len(msg) == 0):
                return 0
            if (len(msg) == 1):
                if (isValid(msg)):
                    return 1
            locTotal = 0
            if (len(msg) == 2):
                if (isValid(msg)):
                    locTotal += 1
            if (isValid(msg[0])):
                locTotal += recNumDecoding(msg[1:])
            if (isValid(msg[0:2])):
                locTotal += recNumDecoding(msg[2:])
            return locTotal  