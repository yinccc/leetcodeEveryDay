def maxsum(nums):
    if not nums:
        return 0

    tempsum=maxsum=nums[0]
    for num in nums[1:]:
        tempsum=max(num,tempsum+num)
        maxsum=max(tempsum,maxsum)
    return maxsum

nums=[-2,1,2,4]
a=maxsum(nums)
print(a)