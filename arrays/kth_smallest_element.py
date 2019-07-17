def kth_smallest_element(array,k):
    '''
    Runtime complexity O(N)
    '''
    temp=[]
    for i in array:
        if(len(temp)!=k):
            temp.append(i)
        elif(i < max(temp)):
            j=temp.index(max(temp))
            temp[j]=i

    return max(temp)

print(kth_smallest_element([7,10,4,3,5,2,20,15],4))
