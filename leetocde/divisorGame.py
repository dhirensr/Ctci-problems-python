def divisorGame(N):
    answer=[0 for i in range(N+1)]
    for i in range(2,N+1):
        for j in range(i-1,0,-1):
            if(i%j==0):
                answer[i]=1+answer[i-j]
    print(answer)
    if(answer[N]%2!=0):
        return True
    else:
        return False

print(divisorGame(2))
