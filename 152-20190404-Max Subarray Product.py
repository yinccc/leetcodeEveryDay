class Solution:
    def maxsubarrayProduct(self,nums):
        if not nums:
            return
        maxproduct=minproduct=globalproduct=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                temp=maxproduct
                maxproduct=max(minproduct*nums[i],nums[i])
                minproduct=min(temp*nums[i],nums[i])
            else:
                maxproduct=max(maxproduct*nums[i],nums[i])
                minproduct=min(minproduct*nums[i],nums[i])
            globalproduct=max(globalproduct,maxproduct)
        return globalproduct

S=Solution()
nums=[1,-2,3,4,0,-5,6,7]
print(S.maxsubarrayProduct(nums))
