class Solution(object):
    def __init__(self):
        self.cntsum = 0

    def helper(self, s, l, r):
        cnt = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l = l - 1
            r = r + 1
            cnt += 1
        return cnt

    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            # even case
            self.cntsum += self.helper(s, i, i)
            # odd case
            self.cntsum += self.helper(s, i, i + 1)
        return self.cntsum
