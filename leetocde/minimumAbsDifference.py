def minimumAbsDifference(arr):
    arr.sort()
    cache = {}
    result = arr[1]-arr[0]
    cache[arr[1]-arr[0]] =[[arr[0],arr[1]]]
    for i in range(1,len(arr)-1):
        if(arr[i+1]-arr[i] <= result):
            result = arr[i+1]-arr[i]
            if (result in cache):
                cache[result].append([arr[i],arr[i+1]])
            else:
                cache[result] = [[arr[i],arr[i+1]]]

    return cache[min(cache.keys())]
print(minimumAbsDifference([40,11,26,27,-20]))
