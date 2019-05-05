class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        found=[0]*len(nums)
        for i in range(len(nums)):
            found[nums[i]-1]=1
        for i in range(len(found)):
            if not found[i]:
                res.append(i+1)
        return res