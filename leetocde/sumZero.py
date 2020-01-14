def sumZero(n):
    odd=0
    result=[]
    if(n%2!=0):
        odd=1
    for i in range(1,n//2+1):
        result.append(i)
        result.append(-i)
    if odd==1:
        result.append(0)
    return result

print(sumZero(5))
