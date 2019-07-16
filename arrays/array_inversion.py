def inversion_count(array):
    count=0
    for idx,i in enumerate(array):
        for j in range(idx,len(array)):
            if(array[idx] > array[j] and idx < j):
                count=count+1
    return count

q=inversion_count([2,4,1,3,5])
print(q)
