def oddCells(n,m,indices):
    array=[[0]*m for i in range(n)]
    for i,j in indices:
        array[i]=[k+1 for k in array[i]]
        for k in array:
            k[j]=k[j]+1
    count=0
    for i in array:
        for j in i:
            if(j%2!=0):
                count+=1
    return count

print(oddCells(2,2,[[0,0],[1,1]]))
