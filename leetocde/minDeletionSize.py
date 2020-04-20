def minDeletionSize(A):
    count= 0
    for i in range(len(A[0])):
        for j in range(1,len(A)):
            if A[j][i] < A[j-1][i]:
                count+=1
                break
    print(count)


minDeletionSize(["zyx","wvu","tsr"])
