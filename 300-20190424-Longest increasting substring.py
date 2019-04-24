class Solution:
    def longest(self,nums):
        if len(nums)==0:
            return 0
        maxlen=1
        dp=[1]*len(nums)
        for i in range(len(nums)):
            templen=0
            for j in range(i):
                if nums[i]>nums[j]:
                    templen=max(templen,dp[j])
            dp[i]=templen+1
            maxlen=max(maxlen,dp[i])
        return maxlen