def pathsum(grid):
    m=len(grid)
    n=len(grid[0])
    for i in range(1,n):
        grid[0][i]+=grid[0][i-1]
    for j in range(1,m):
        grid[j][0]+=grid[j-1][0]
    for i in range(1,n):
        for j in range(1,m):
            grid[j][i]+=min(grid[j-1][i],grid[j][i-1])
    return grid[-1][-1]


b=[[1,3,1],[1,5,1],[4,2,1]]
print(pathsum(b))