def longestCommonSubsequence(text1,text2):
    val_matrix= [[0]* len(text2) for j in range(len(text1))]

    for i in range(len(text1)):
        if text2[0] in text1[:i+1]:
            val_matrix[i][0] =1
    for i in range(len(text2)):
        if text1[0] in text2[:i+1]:
            val_matrix[0][i] =1

    for i in range(1,len(text1)):
        for j in range(1,len(text2)):
            if text1[i]==text2[j]:
                val_matrix[i][j]=val_matrix[i-1][j-1]+1
            else:
                val_matrix[i][j]=max(val_matrix[i-1][j],val_matrix[i][j-1])

    return val_matrix[len(text1)-1][len(text2)-1]

print(longestCommonSubsequence("a","n"))
