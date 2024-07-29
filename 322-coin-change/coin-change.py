class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0

        n = amount
        dp = [0] *(n+1)

        for i in range(1,n+1):
            dp[i] = float(inf)

            for coin in coins:
                if (
                    coin <= i and
                    dp[i - coin] != float(inf)
                ):
                    dp[i] = min(dp[i], 1+dp[i-coin])


        if dp[n] == float(inf):
            return -1

        return dp[n]