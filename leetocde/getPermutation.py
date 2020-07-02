def getPermutation(n,k):
    factorial= [0 for i in range(n)]
    factorial[0] = 1
    for i in range(1,n):
        factorial[i] = (i+1)*factorial[i-1]
    outputs = [i+1 for i in range(n)]
    result = ""
    for i in range(1,n):
        temp1 = n-i-1
        temp = factorial[temp1]
        u = 0
        while k>temp:
            k = k - temp
            u+=1
        result += str(outputs[u])
        outputs.remove(outputs[u])
    result+= str(outputs[0])
    return result

getPermutation(3,2)
