def BubbleSort(nums):
    length=len(nums)
    if length<=1:
        return nums
    for i in range(length):
        for j in range(length-i-1):
            if nums[j]>nums[j + 1]:
                nums[j], nums[j + 1]= nums[j + 1], nums[j]
    return nums
#Time O(n2)
#Space O(1)
arr=[9,8,7,6,5,4,3,2,1]
print(BubbleSort(arr))


def BubbleSort2(nums):
    if len(nums)<=1:
        return nums
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums
print(BubbleSort2(arr))


def BubbleSort3(nums):
    if len(nums)<=1:
        return nums
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

print(BubbleSort3(arr))
