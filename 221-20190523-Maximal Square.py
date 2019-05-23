matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
dp=[[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]
print(len(matrix),len(matrix[0]))
print(len(dp),len(dp[0]))

maxNumber=0
def ThreeMin(i, j, k):
    return min(min(int(i), int(j)), int(k))

for i in range(len(matrix)):
    dp[i][0]=matrix[i][0]
    if matrix[i][0]=='1':
        maxNumber=1
for j in range(len(matrix[0])):
    dp[0][j]=matrix[0][j]
    if matrix[0][j]=='1':
        maxNumber=1

for i in range(1,len(matrix)):
    for j in range(1,len(matrix[0])):
        dp[i][j]=ThreeMin(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
        if dp[i][j]>maxNumber:
            maxNumber=dp[i][j]
print(maxNumber)


class Solution(object):
    def ThreeMin(self, i, j, k):
        return min(min(int(i), int(j)), int(k))

    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        maxNumber = 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for x in range(n)] for y in range(m)]

        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0] == 1:
                maxNumber = 1

        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            if dp[0][j] == 1:
                maxNumber = 1

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '0':
                    continue
                dp[i][j] = self.ThreeMin(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                if dp[i][j] > maxNumber:
                    maxNumber = dp[i][j]
        return maxNumber ** 2

s=Solution()
print(s.maximalSquare(matrix))