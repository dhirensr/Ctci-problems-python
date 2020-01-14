def min_time_for_a_to_b(a,b,count):
    if(a[0]>b[0]):
        a,b=b,a
    while(a[0]!=b[0] and a[1]!=b[1] and a!=b): # walk along  the diagonal
        count+=1
        a[0]=a[0]+1
        a[1]=a[1]+1
    if(a==b):
        return count
    if(a[0]==b[0]): #x direction matches i.e walk along y
        count+=abs(a[1]-b[1])
        return count
    elif(a[1]==b[1]): #y direction matches i.e walk along x
        count+=abs(a[0]-b[0])
        return count
    else:
        if(a[1] <b[1]):
            return min_time_for_a_to_b([a[0]+1,a[1]+1],b,count)
        else:
            return min_time_for_a_to_b([a[0]+1,a[1]-1],b,count)

print(min_time_for_a_to_b([3,2],[-2,2 ],0))
