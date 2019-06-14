def MergeSort(ls):
    # 合并左右子序列函数
    def merge(arr, left, mid, right):
        temp = []  # 中间数组
        i = left  # 左段子序列起始
        j = mid + 1  # 右段子序列起始
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= right:
            temp.append(arr[j])
            j += 1
        for i in range(left, right + 1):  # !注意这里，不能直接arr=temp,他俩大小都不一定一样
            arr[i] = temp[i - left]

    # 递归调用归并排序
    def mSort(arr, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        mSort(arr, left, mid)
        mSort(arr, mid + 1, right)
        merge(arr, left, mid, right)

    n = len(ls)
    if n <= 1:
        return ls
    mSort(ls, 0, n - 1)
    return ls


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
        while j<=right:
            tmp.append(nums[j])
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
a=[9,8,7,6,5,4,3,2,1]
print(MergeSort(a))
