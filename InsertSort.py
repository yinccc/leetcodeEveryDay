def InsertSort(ls):
    n=len(ls)
    if n<=1:
        return ls
    for i in range(1,n):
        j=i
        target=ls[i]            #每次循环的一个待插入的数
        while j>0 and target<ls[j-1]:       #比较、后移，给target腾位置
            ls[j]=ls[j-1]
            j=j-1
        ls[j]=target            #把target插到空位
    return ls
arr=[9,8,7,6,5,4,3,2,1]
print(InsertSort(arr))

def InsertSort2(nums):
    if len(nums)<=1:
        return nums
    for i in range(1,len(nums)):
        j=i
        target=nums[i]
        while j>0 and nums[j-1]>target:
            nums[j]=nums[j-1]
            j=j-1
        nums[j]=target
    return nums
print(InsertSort2(arr))


def InsertSort3(nums):
    if len(nums)<=1:
        return nums
    for i in range(1,len(nums)):
        j=i
        target=nums[i]
        while j>0 and nums[j-1]>target:
            nums[j]=nums[j-1]
            j=j-1
        nums[j]=target
    return nums
print(InsertSort3(arr))

def InsertSort4(nums):
    if len(nums)<=1:
        return nums

    for i in range(1,len(nums)):
        j=i
        target=nums[i]
        while j>0 and nums[j-1]>target:
            nums[j]=nums[j-1]
            j=j-1
        nums[j]=target
    return nums


def InsertSort5(nums):
    if len(nums)<=1:
        return nums
    for i in range(1,len(nums)):
        j=i
        target=nums[i]
        while j>0 and nums[j-1]>target:
            nums[j]=nums[j-1]
            j=j-1
        nums[j]=target
    return nums
