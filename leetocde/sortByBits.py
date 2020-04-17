def int_to_binary(num):
    k=0
    count = 0
    while num > 2**k:
        k+=1
    if num == 2**k:
        count =1
    else:
        for i in range(k-1,-1,-1):
            if num >= 2**i:
                count+=1
                num = num - 2**i
    return count



def sortByBits(arr):
    output = []
    for i in arr:
        output.append([i,int_to_binary(i)])
    output.sort(key=lambda x: (x[1],x[0]))
    print(output)
    for idx,i in enumerate(output):
        output[idx] = i[0]
    print(output)
    return output

sortByBits([1024,512,256,128,64,32,16,8,4,2,1])
