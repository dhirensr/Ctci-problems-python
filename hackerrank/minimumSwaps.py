def minimumSwaps(arr):
    #sorted_arr = sorted(arr)
    index_map={}
    count =0
    for i in range(len(arr)):
        index_map[arr[i]] = i
    #print(index_map)
    for i in range(len(arr)):
        if arr[i]!=i+1:
            index =index_map[i+1]
            index_map[arr[i]]= index
            index_map[i+1] = i
            temp = arr[i]
            arr[i]=i+1
            arr[index]=temp
            count+=1

    return count


print(minimumSwaps([7,1,3,2,4,5,6]))
