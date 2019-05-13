class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        d,count,l = {},0,len(tasks)
        if not n: return l
        for c in tasks:
            if c in d:
                d[c] +=1
            else:
                d[c] = 1
        max_val = max(d.values())
        for i in d.values():
            if i == max_val:
                count+=1
        return max((max_val-1)*(n+1)+count,l)