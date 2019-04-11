class Solution:
    def numberOfIslands(self,grid):
        if not grid:
            return 0

        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    self.dfs(i,j,grid)
                    count+=1
        return count

    def dfs(self,i,j,grid):
        if i<0 or j<0 or i>=len(grid) or j >=len(grid[0]) or grid[i][j]!='1':
            return
        grid[i][j]="#"
        self.dfs(i+1,j,grid)
        self.dfs(i-1, j, grid)
        self.dfs(i, j+1, grid)
        self.dfs(i, j-1, grid)


class Solution2(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
S=Solution()
print(S.numberOfIslands(grid))
grid=[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
s2=Solution2()
print(s2.numIslands(grid))