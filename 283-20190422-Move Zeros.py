class Solution:
    def moveZeros(self,nums):
        zero=0
        for non_zero in range(len(nums)):
            if nums[non_zero]==0:
                continue

            if nums[zero]==0:
                nums[zero],nums[non_zero]=nums[non_zero],nums[zero]
            zero+=1

        return nums


nums=[0,1,2,3,0]
S=Solution()
print(S.moveZeros(nums))
