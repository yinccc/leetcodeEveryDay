class Solution:
    def KthLargestElement(self,nums,k):
        return sorted(nums,reverse=True)[k-1]


nums=[1,5,4,3,5,7,8,4,7,9,2]
S=Solution()
print(S.KthLargestElement(nums,1))