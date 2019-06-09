class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1,len2=len(word1)+1,len(word2)+1
        dp=[[0 for x in range(len2)] for y in range(len1)]
        for i in range(len1):
            dp[i][0]=i
        for j in range(len2):
            dp[0][j]=j
        for i in range(1,len1):
            for j in range(1,len2):
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+(word1[i-1]!=word2[j-1]))
        return dp[-1][-1]


# -*- coding:utf-8 -*-

class MinCost:
    def findMinCost(self, A, B,c0, c1, c2):
        # write code here
        row=len(A)+1
        column=len(B)+1
        dp=[[0 for x in range(column)] for y in range(row)]
        for i in range(row):
            dp[i][0]=c1*i
        for j in range(column):
            dp[0][j]=c0*j
        for i in range(1,row):
            for j in range(1,column):
                if A[i-1]==B[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=dp[i-1][j-1]+c2
                dp[i][j]=min(dp[i][j],dp[i][j-1]+c0,dp[i-1][j]+c1)
        return dp[-1][-1]