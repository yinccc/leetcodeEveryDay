def jump(nums):
    if not nums:
        return False

    m=0
    for i,n in enumerate(nums):
        if i>m:
            return False
        m=max(m,i+n)
    return True


nums=[1,2,0,2]
print(jump(nums))