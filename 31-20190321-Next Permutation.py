#找到第一个大于它的
def nextPermutation(nums):
    i=j=len(nums)-1
    while i>0 and nums[i]<=nums[i-1]:
        i-=1
    if i>0:
        while nums[j]<=nums[i-1]:
            j-=1
    nums[i-1],nums[j]=nums[j],nums[i-1]
    nums[i:]=reversed(nums[i:])
    return nums

nums=[1,1,5]
print(nextPermutation(nums))