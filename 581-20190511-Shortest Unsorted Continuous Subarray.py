class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sort_nums=sorted(nums)
        compare=list(i==j for i,j in zip(nums,sort_nums))
        ans=([i for i in range(len(compare)) if compare[i]==0])
        if not ans: return 0
        else:  return (max(ans)-min(ans)+1)