def countsquares(matrix):
    count=0
    square_matrix=[[0]*(len(matrix[0])+1) for i in range(len(matrix)+1)]
    for i in range(1,len(matrix)+1):
        for j in range(1,len(matrix[0])+1):
            #print(i,j)
            #print(square_matrix)
            if(matrix[i-1][j-1]==1):
                #print(i,j)
                square_matrix[i][j]=min(square_matrix[i-1][j],square_matrix[i][j-1],square_matrix[i-1][j-1])+1
            else:
                square_matrix[i][j]=0
    for i in square_matrix:
        for j in i:
            count+=j
    return count




countsquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]])
