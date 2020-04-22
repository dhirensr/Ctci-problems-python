def rotatedDigits(N):
    cache={}
    cache[0]=0
    cache[1]=1
    cache[2]=5
    cache[5]=2
    cache[3]=None
    cache[4]=None
    cache[6]=9
    cache[7]=None
    cache[8]=8
    cache[9]=6
    count=0
    result_set=set()
    for i in range(N+1):
        result=""
        temp=0
        for j in str(i):
            if cache[int(j)]==None:
                temp=1
                break
            result+=str(cache[int(j)])
        if result and int(result)!=i and temp!=1:
            count+=1
    print(count)

rotatedDigits(857)
