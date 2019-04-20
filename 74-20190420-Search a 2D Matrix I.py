class Solution:
    def SearchMatrix(self,matrix,target):
        if not matrix or not matrix[0]:
            return False
        row=len(matrix)
        column=len(matrix[0])
        low=0
        high=row*column-1
        while high>=low:
            k=(low+high)//2
            i,j=divmod(k,column)
            mid=matrix[i][j]

            if mid>target:
                high=k-1
            elif mid <target:
                low=k+1
            else:
                return True
        return False


matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,50]]
S=Solution()
print(S.SearchMatrix(matrix,50))