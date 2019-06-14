def SelectSort(arr):
    length=len(arr)
    if length<=1:
        return arr
    for i in range(length-1):
        minindex=i
        for j in range(i+1,length):
            if arr[j]<arr[minindex]:
                minindex=j
        if minindex!=i:
            arr[i],arr[minindex]=arr[minindex],arr[i]
    return arr
#Time O(n2)
#Space O(1)
arr=[9,8,7,6,5,4,3,2,1]
print(SelectSort(arr))


def SelectSort2(nums):
    if len(nums)<=1:
        return nums
    for i in range(len(nums)-1):
        minindex=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[minindex]:
                minindex=j
        if minindex!=i:
            nums[i],nums[minindex]=nums[minindex],nums[i]
    return nums
print(SelectSort2(arr))

def SelectSort3(nums):
    if len(nums)<=1:
        return nums
    for i in range(len(nums)-1):
        minindex=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[minindex]:
                minindex=j
        if minindex!=i:
            nums[i],nums[minindex]=nums[minindex],nums[i]
    return nums
print(SelectSort3(arr))

def SelectSort4(nums):
    if len(nums)<=1:
        return nums
    for i in range(len(nums)-1):
        minindex=i
        for j in range(i+1,len(nums)):
            if nums[j]<nums[minindex]:
                minindex=j
        if minindex!=i:
            nums[i],nums[minindex]=nums[minindex],nums[i]
    return nums

print(SelectSort4(arr))