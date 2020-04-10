paths = []
cache = {}
def helper(obstacleGrid,output,m,n):
    if (m == len(obstacleGrid)-1 and n == len(obstacleGrid[0])-1):
        output.append((m,n))
        paths.append(output)
    else:
        output.append((m,n))
        cache[(m,n)] = output
        if(n!=len(obstacleGrid[0])-1 and obstacleGrid[m][n+1] !=1):
            helper(obstacleGrid,cache[(m,n)],m,n+1)
        if( m != len(obstacleGrid)-1 and obstacleGrid[m+1][n]!=1):
            helper(obstacleGrid,cache[(m,n)],m+1,n)

def helper2(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])

    if obstacleGrid[0][0] == 1:
        return 0
    obstacleGrid[0][0] = 1

    for i in range(1,m):
        obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

    for j in range(1, n):
        obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

    # Starting from cell(1,1) fill up the values
    # No. of ways of reaching cell[i][j] = cell[i - 1][j] + cell[i][j - 1]
    # i.e. From above and left.
    for i in range(1,m):
        for j in range(1,n):
            if obstacleGrid[i][j] == 0:
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
            else:
                obstacleGrid[i][j] = 0

    # Return value stored in rightmost bottommost cell. That is the destination.
    return obstacleGrid[m-1][n-1]

def uniquePathsWithObstacles(obstacleGrid):
    """
    https://leetcode.com/problems/unique-paths-ii/
    """
    if obstacleGrid[0][0] == 1:
        return 0
    if len(obstacleGrid)-1 ==0 and len(obstacleGrid[0])-1 ==0:
        return 1
    helper(obstacleGrid,[],0,0)
    output = helper2(obstacleGrid)
    print(output)
    return len(paths)


print(uniquePathsWithObstacles([[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0]]))
