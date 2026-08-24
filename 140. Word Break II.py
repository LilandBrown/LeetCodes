class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        arr =  [[] for _ in range(len(s) + 1)]
        arr [0] = [""]
        for i in range (1, len(s) + 1):
            for j in range(1, min(i+1, 11)):
                if ( [arr [i - j] != "" or i - j == 0] and s[i - j : i ] in wordDict):
                    if arr [i - j] == [""]:
                        arr[i].extend(x + s[i - j : i] for x in arr[i-j]) 
                    else:
                        arr[i].extend(x + " " + s[i - j : i] for x in arr[i-j]) 

        return arr[len(s)]