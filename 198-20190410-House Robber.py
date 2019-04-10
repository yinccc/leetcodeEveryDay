class Solution:
    def houseRobber(self,nums):
        n=len(nums)
        if n==0:
            return 0
        elif n==1:
            return nums[0]
        rob=[0]*n
        rob[0]=nums[0]
        rob[1]=max(nums[:2])
        for i in range(2,n):
            rob[i]=max(nums[i]+rob[i-2],rob[i-1])
        return rob[n-1]

nums=[2,3,4,5,6]
S=Solution()
print(S.houseRobber(nums))