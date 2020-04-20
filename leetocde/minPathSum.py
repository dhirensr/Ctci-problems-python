def minPathSum(grid):
    output= [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    #print(output)
    output[0][0] = grid[0][0]
    for i in range(1,len(grid[0])):
        output[0][i] = output[0][i-1] + grid[0][i]
    for i in range(1,len(grid)):
        output[i][0] = output[i-1][0] + grid[i][0]
    for i in range(1,len(grid)):
        for j in range(1,len(grid[0])):
            output[i][j]  =min(output[i-1][j],output[i][j-1]) + grid[i][j]
    return output[len(grid)-1][len(grid[0])-1]


print(minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))
