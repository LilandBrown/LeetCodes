class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def calc(list, remainder, factorial):
            """
            :type list: list
            :type remainder: int
            :factorial: int
            :rtype: st
            """
            if len(list) == 1:
                return list[0]
            else :
                return list.pop(remainder // factorial) + calc(list, remainder % factorial, factorial // len(list))
        numbers = [str(i) for i in range(1, n + 1)]
        result = 1
        for i in range(2, n ):
            result *= i
        return calc(numbers, k - 1, result)           