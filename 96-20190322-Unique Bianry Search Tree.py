import time
def countTrees1(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    Result = 0
    for i in range(n):
        LeftTrees = countTrees1(i)
        RightTrees = countTrees1(n - i - 1)
        Result += LeftTrees * RightTrees
    return Result

time1=time.time()
print(countTrees1(15))
time2=time.time()


def countTrees2(n, cache):
    if n == 0:
        return 1
    if n == 1:
        return 1

    if n in cache: #-1 means we don't know countTrees(n) yet.
        return cache[n]

    Result = 0
    for i in range(n):
        LeftTrees = countTrees2(i, cache)
        RightTrees = countTrees2(n - i - 1, cache)
        Result += LeftTrees * RightTrees
    cache[n] = Result
    return Result
cache={}

time3=time.time()
print(countTrees2(15,cache))
time4=time.time()

class Solution:
    def numTrees(self, n: int) -> int:
        res=[0]*(n+1)
        res[0]=1
        for i in range(1,n+1):
            for j in range(i):
                res[i]+=res[j]*res[i-j-1]
        return res[n]

S=Solution()

time5=time.time()
print(S.numTrees(15))
time6=time.time()

print(time2-time1)
print(time4-time3)
print(time6-time5)