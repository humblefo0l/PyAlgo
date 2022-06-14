"""
123. Best Time to Buy and Sell Stock III
Hard

5991

122

Add to List

Share
You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).



Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

"""
import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        k = 2
        dp = [[0 for i in prices] for i in range(k+1)]
        for t in range(1, k+1):
            max_value = -sys.maxsize
            for d  in range(1, len(prices)):

                if dp[t-1][d-1] - prices[d-1] > max_value:
                    max_value = dp[t-1][d-1] - prices[d-1]


                if max_value + prices[d] > dp[t][d-1]:
                    dp[t][d] = max_value + prices[d]
                else:
                    dp[t][d] = dp[t][d-1]

        return dp[k][len(prices)-1]


s = Solution()
prices = [3,3,5,0,0,3,1,4]
print(s.maxProfit(prices))