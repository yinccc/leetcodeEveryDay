def BubbleSort(nums):
    if len(nums)<=1:
        return nums
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

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

def InsertSort(nums):
    if len(nums)<=1:
        return nums
    for i in range(1,len(nums)):
        j=i
        target=nums[i]
        while j>0 and nums[j-1]>nums[j]:
            nums[j]=nums[j-1]
            j-=1
        nums[j]=target
    return nums

def QuickSort(nums):
    if len(nums)<=1:
        return nums
    def partition(nums,left,right):
        key=left
        while left<right:
            while left<right and nums[right]>nums[key]:
                right-=1
            while left<right and nums[left]<nums[key]:
                left+=1
            nums[left],nums[right]=nums[right],nums[left]
        nums[left],nums[key]=nums[key],nums[left]
        return left
    def quickSort(nums,left,right):
        if left>right:
            return
        mid=partition(nums,left,right)
        quickSort(nums,0,mid-1)
        quickSort(nums,mid+1,right)
    quickSort(nums,0,len(nums)-1)
    return nums

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
    def mergeSort(nums,left,right):
        if left<=right:
            return
        mid=int((left+right)/2)
        mergeSort(nums,mid+1,right)
        mergeSort(nums,left,mid)
        merge(nums,left,mid,right)

    mergeSort(nums,0,len(nums)-1)
    return nums

a=[9,8,7,6,5,4,3,2,1]
print(BubbleSort(a))
print(SelectSort(a))
print(InsertSort(a))
print(QuickSort(a))
print(MergeSort(a))