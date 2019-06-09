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