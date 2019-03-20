def subsets(nums):
    subsets = [[]]
    for n in nums:
        subsets += [s + [n] for s in subsets]
    return subsets


x=[1,2,3]
print(subsets(x))