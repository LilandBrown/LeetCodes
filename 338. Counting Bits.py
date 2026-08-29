class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        :timeComplexity and spaceComplexity of O(n)
        """
        arr = [0] * (n+1)
        arr [0] = 0
        if n == 0:
            return arr
        arr [1] = 1
        sigBit = 1
        for i in range(2, n + 1):
            if i % sigBit == 0:
                arr [i] = 1
                sigBit *= 2
            else:
                arr [i] = arr[sigBit] + arr[i - sigBit]
        return arr