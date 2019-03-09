class Solution2(object):
    def twoSum(self, nums, target):
        a = {}
        for i, num in enumerate(nums):
            if target - num in a:
                return [a[target - num], i]
            else:
                a[num] = i


nums = [3,3]
target=6
s2=Solution2()
print(s2.twoSum(nums,target))
