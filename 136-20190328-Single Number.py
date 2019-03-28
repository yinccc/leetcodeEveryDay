class Solution:
    #hash table
    def singleNumber1(self,nums):
        dic={}
        for num in nums:
            dic[num]=dic.get(num,0)+1
        for key,val in dic.items():
            if val==1:
                return key
    #math method
    def singleNumber2(self,nums):
        return 2*sum(set(nums))-sum(nums)

    #bit method
    def singleNumber3(self,nums):
        a=0
        for num in nums:
            a^=num
        return a

S=Solution()
nums=[1,1,2,2,4,5,6,6,5,4,7,8,9,8,9]
print(S.singleNumber1(nums))
print(S.singleNumber2(nums))
print(S.singleNumber3(nums))


