def trip2(n,k,array):
    possible_options=range(1,k+1)
    for i in range(n):
        if i==0:
            for j in possible_options:
                if(array[i+1]!=j):
                    array[i]=j
                    break
        elif i==n-1:
            for j in possible_options:
                if(array[i-1]!=j):
                    array[i]=j
                    break
        else:
            for j in possible_options:
                if(array[i-1] !=j and array[i+1]!=j):
                    array[i]=j
                    break

    if any(i==-1 for i in array):
        print('NO')
    else:
        print('YES')
        print(*array)

trip2(6,4,[-1,-1,4,-1,2,-1])
