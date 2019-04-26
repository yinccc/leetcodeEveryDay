class Solution:
    def coinsChange(self,coins,amount):
        maxNums=amount+1
        dp=[maxNums]*maxNums
        dp[0]=0
        for i in range(1,maxNums):
            for j in range(len(coins)):
                if coins[j]<=i:
                    dp[i]=min(dp[i],dp[i-coins[j]]+1)
        return -1 if dp[amount]>amount else dp[amount]