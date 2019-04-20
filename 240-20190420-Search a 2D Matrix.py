########################Solution1(Binary Search) O(mlog(n))
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False

        for r in matrix:
            if r[-1] < target:
                continue

            if r[0] > target:
                return False

            if self.binarySearch(r, target):
                return True

        return False

    def binarySearch(self, row, target):
        if not row:
            return False

        mid = len(row) // 2

        if target == row[mid]:
            return True
        elif target > row[mid]:
            return self.binarySearch(row[mid + 1:], target)
        else:
            return self.binarySearch(row[:mid], target)

        return False

####################Solution2 O(m+n)
class Solution2:
    def SearchMatrix(self,matrix,target):
        if matrix and matrix[0]:
            row=len(matrix)
            column=len(matrix[0])
            i=row-1
            j=0
            while row>i>=0 and column>j:
                if matrix[i][j]>target:
                    i=i-1
                elif matrix[i][j]<target:
                    j=j+1
                else:
                    return True
        return False

matrix=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
S1=Solution()
S2=Solution2()
print(S1.searchMatrix(matrix,17))
print(S2.SearchMatrix(matrix,17))