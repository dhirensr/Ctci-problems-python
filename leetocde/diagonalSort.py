def sort(mat,start,end):
    m,n =len(mat),len(mat[0])
    i = start
    j = end
    elements = []
    while (i <m and j <n):
        elements.append(mat[i][j])
        i+=1
        j+=1
    elements.sort()
    i = start
    j = end
    k=0
    while (i <m and j <n):
        mat[i][j] = elements[k]
        i+=1
        j+=1
        k+=1
    return mat


def diagonalSort(mat):
    """
    https://leetcode.com/problems/sort-the-matrix-diagonally/
    """
    m , n = len(mat), len(mat[0])
    for i in range(1,m):
        mat = sort(mat,i,0)
    for i in range(n):
        mat = sort(mat,0,i)
    return mat


print(diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
