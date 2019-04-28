class Solution:
    def counting(self,num):
        dp=[0 for _ in range(num+1)]
        for i in range(num+1):
            if i%2==0:
                dp[i]=dp[i//2]
            else:
                dp[i]=dp[i//2]+1
        return dp