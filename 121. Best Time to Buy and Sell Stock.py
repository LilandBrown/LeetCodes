class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        mini = prices[0]
        maxi = prices[0]
        for i in prices:
            if i < mini:
                mini = i
                maxi = i
            elif i > maxi:
                maxi = i
                profit = max(maxi - mini, profit)
        return profit