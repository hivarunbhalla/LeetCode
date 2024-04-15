import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_min = float(inf)
        right_max = 0
        i = 0
        while(i < len(prices)):
            left_min = min(prices[i], left_min)
            right_max = max(prices[i]-left_min, right_max)
            i+=1

        return right_max
