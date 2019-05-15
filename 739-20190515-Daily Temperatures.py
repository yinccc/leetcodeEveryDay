class Solution(object):
    def dailyTemperatures(self, nums):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res=[0]*len(nums)
        stack=[]
        for i in range(len(nums)):
            while stack and nums[i]>nums[stack[-1]]:
                cur=stack.pop()
                res[cur]=i-cur
            stack.append(i)
        return res