a=[9,8,7,6,5,4,3,2,1]
b=[4,5,3,2,1,8,6,7,9,0]

def BubbleSort(nums):
    if len(nums)<=1:
        return nums
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

print(BubbleSort(a))

def SelectSort(nums):
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

print(SelectSort(a))

def InsertSort(nums):
    if len(nums)<=1:
        return nums
    for i in range(1,len(nums)):
        j=i
        target=nums[i]
        while j>0 and nums[j]<nums[j-1]:
            nums[j]=nums[j-1]
            j-=1
        nums[j]=target
    return nums

print(InsertSort(a))

def QuickSort(nums):
    if len(nums)<=1:
        return nums
    def partition(nums,left,right):
        key=left
        while left<right:
            while left<right and nums[right]>=nums[key]:
                right-=1
            while left<right and nums[left]<=nums[key]:
                left+=1
            nums[left],nums[right]=nums[right],nums[left]
        nums[key],nums[left]=nums[left],nums[key]
        return left
    def quickSort(nums,left,right):
        while left>right:
            return
        mid=partition(nums,left,right)
        quickSort(nums,mid+1,right)
        quickSort(nums,left,mid-1)
    quickSort(nums,0,len(nums)-1)
    return nums
print(QuickSort(a))
print(QuickSort(b))

def MergeSort(nums):
    if len(nums)<=1:
        return nums
    def merge(nums,left,mid,right):
        tmp=[]
        i=left
        j=mid+1
        while i<=mid and j<=right:
            if nums[i]<=nums[j]:
                tmp.append(nums[i])
                i+=1
            else:
                tmp.append(nums[j])
                j+=1
        while i<=mid:
            tmp.append(nums[i])
            i+=1
        while j<=right:
            tmp.append(nums[j])
            j+=1
        for i in range(left,right+1):
            nums[i]=tmp[i-left]

    def sort(nums,left,right):
        if left>=right:
            return
        mid=(left+right)//2
        sort(nums,left,mid)
        sort(nums,mid+1,right)
        merge(nums,left,mid,right)

    sort(nums,0,len(nums)-1)
    return nums

print(MergeSort(b))


def QuickSort2(nums):
    if len(nums)<=1:
        return nums
    def partition(nums,left,right):
        key=left
        while left<right:
            while left<right and nums[right]>=nums[key]:
                right-=1
            while left<right and nums[left]<=nums[key]:
                left+=1
            nums[right],nums[left]=nums[left],nums[right]
        nums[key],nums[left]=nums[left],nums[key]
        return left

    def quickSort(nums,left,right):
        while left>right:
            return
        mid=partition(nums,left,right)
        quickSort(nums,left,mid-1)
        quickSort(nums,mid+1,right)
    quickSort(nums,0,len(nums)-1)
    return nums

def MergeSort2(nums):
    if len(nums)<=1:
        return nums
    def merge(nums,left,mid,right):
        tmp=[]
        i=left
        j=mid+1
        while i<=mid and j<=right:
            if nums[i]<=nums[j]:
                tmp.append(nums[i])
                i+=1
            else:
                tmp.append(nums[j])
                j+=1
        while i<=mid:
            tmp.append(nums[i])
            i+=1
        while j<=right:
            tmp.append(nums[j])
            j+=1
        for i in range(left,right+1):
            nums[i]=tmp[i-left]

    def sort(nums,left,right):
        if left>=right:
            return
        mid=(left+right)//2
        sort(nums,left,mid)
        sort(nums,mid+1,right)
        merge(nums,left,mid,right)

    sort(nums,0,len(nums)-1)
    return nums

c=[4,5,3,2,1,8,6,7,9,0,100]
print(QuickSort2(c))
print(MergeSort2(c))

