def leftMostColumnWithOne(matrix):
    n= len(matrix)
    m= len(matrix[0])
    i=0
    j=m-1
    count = 0
    while i<n and j>=0:
        value = matrix[i][j]
        if value==1:
            j=j-1
        else:
            i=i+1
    if j !=m-1:
        return j+1
    else:
        return -1


print(leftMostColumnWithOne([[0,0],[1,1]]))
