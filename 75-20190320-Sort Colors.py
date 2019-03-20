#two pass
def SortColors(nums):
    numZeros=0
    numOnes=0
    numTwos=0
    for i in range(len(nums)):
        if nums[i]==0:
            numZeros+=1
        if nums[i]==1:
            numOnes+=1
        if nums[i]==2:
            numTwos+=1
    i=0
    while(i<len(nums)):
        if i<numZeros:
            nums[i]=0
            i=i+1
        if i<numZeros+numOnes and i>=numZeros:
            nums[i]=1
            i=i+1
        if i<len(nums) and i>=numZeros+numOnes:
            nums[i]=2
            i=i+1
    return nums

#one pass
def SortColorsTwo(nums):
    red,white,blue=0,0,len(nums)-1
    while white<blue:
        if nums[white]==0:
            nums[white],nums[red]=nums[red],nums[white]
            red+=1
            white+=1
        elif nums[white]==1:
            white+=1
        else:
            nums[white],nums[blue]=nums[blue],nums[white]
            blue-=1
    return nums

nums=[0,1,2,0,1,2,0,1,0]
print(SortColors(nums))
print(SortColorsTwo(nums))
