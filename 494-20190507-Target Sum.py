class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        numSum=sum(nums)
        if(numSum<S):
            return 0
        shift=numSum
        maxSum=numSum*2+1
        ways=[0]*maxSum
        ways[shift]=1
        for num in nums:
            tmp=[0]*maxSum
            for i in range(num,maxSum-num):
                tmp[i+num]+=ways[i]
                tmp[i-num]+=ways[i]
            ways=tmp
        return ways[S+shift]