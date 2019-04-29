class Solution:
    def topKfrequent(self,nums,k):
        dic={}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]]=1
            else:
                dic[nums[i]]+=1
        sortList=sorted(dic.items(),key=lambda x:x[1],reverse=True)
        return [item[0] for item in sortList[:k]]