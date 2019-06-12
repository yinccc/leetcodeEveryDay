def QuickSort(ls):
    def partition(arr, left, right):
        key = left  # 划分参考数索引,默认为第一个数，可优化
        while left < right:
            while left < right and arr[right] >= arr[key]:
                right -= 1
            while left < right and arr[left] <= arr[key]:
                left += 1
            (arr[left], arr[right]) = (arr[right], arr[left])
        (arr[left], arr[key]) = (arr[key], arr[left])
        return left

    def quicksort(arr, left, right):  # 递归调用
        if left >= right:
            return
        mid = partition(arr, left, right)
        quicksort(arr, left, mid - 1)
        quicksort(arr, mid + 1, right)

    # 主函数
    n = len(ls)
    if n <= 1:
        return ls
    quicksort(ls, 0, n - 1)
    return ls

arr=[9,8,7,6,5,4,3,2,1]
print(QuickSort(arr))

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
        nums[left],nums[key]=nums[key],nums[left]
        return left
    def quickSort(nums,left,right):
        if left>=right:
            return
        mid=partition(nums,left,right)
        quickSort(nums,left,mid-1)
        quickSort(nums,mid+1,right)

    quickSort(nums,0,len(nums)-1)
    return nums

print(QuickSort2(arr))


def QuickSort3(nums):
    if len(nums)<=1:
        return nums
    def partition(nums,left,right):
        key=left
        while left<right:
            while left<right and nums[right]>=nums[key]:
                right-=1
            while left<right and nums[left]<=nums[key]:
                left+=1
            nums[right],nums[left]=nums[left],nums[key]
        nums[left],nums[key]=nums[key],nums[left]
        return left
    def quickSort(nums,left,right):
        if left>right:
            return
        mid=partition(nums,left,right)
        quickSort(nums,mid+1,right)
        quickSort(nums,left,mid-1)

    quickSort(nums,0,len(nums)-1)
    return nums
print(QuickSort3(arr))