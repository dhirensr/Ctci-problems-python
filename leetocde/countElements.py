def countElements(arr):
    arr.sort()
    count = 0
    temp=0
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            if arr[i] + 1 == arr[i+1]:
                count+=temp+1
            temp = 0
        else:
            temp+=1
    return count

print(countElements([1,2,3]))
