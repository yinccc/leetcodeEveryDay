class Solution:
    def __init__(self):
        self.f={}
    def fib(self, N: int) -> int:
        if N in self.f:
            return self.f[N]
        if N==0:
            return 0
        if N==1:
            return 1
        self.f[N]=self.fib(N-1)+self.fib(N-2)
        return self.f[N]

S=Solution()
print(S.fib(3))