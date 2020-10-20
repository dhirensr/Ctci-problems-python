def kadanes_algo(array):
    output= [array[0]]
    contiguous_sum = array[0]
    for i in range(1,len(array)):
        max_element = max(array[i],array[i]+output[i-1])
        output.append(max_element)
        if max_element > contiguous_sum:
            contiguous_sum = max_element
    return contiguous_sum


print(kadanes_algo([1,2,3,-2,5]))
