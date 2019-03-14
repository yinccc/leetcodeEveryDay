class Solution:
    def rotate(self,matrix):
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]


a=[[1,2,3],[4,5,6],[7,8,9]]
s=Solution()
b=s.rotate(a)
print(a)