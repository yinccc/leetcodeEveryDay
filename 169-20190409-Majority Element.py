class Solution:
    def majorElements(self,nums):
        dic={}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]]=1
            else:
                dic[nums[i]]+=1
        return max(dic.keys(),key=dic.get)


S=Solution()
nums=[2,2,2,2,2,5,6,7,4]
print(S.majorElements(nums))

