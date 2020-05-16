def kadanes_algo(array):
    result= array[0]
    temp = array[0]
    for i in array[1:]:
        temp = max(temp+i,i)
        result=  max(result,temp)
    return result

def maxSubArraySumCircular(A):
    k = kadanes_algo(A)
    negated_A=[]
    array_sum = 0
    for i in A:
        negated_A.append(i*-1)
        array_sum+=i
    array_sum += kadanes_algo(negated_A)
    #print(array_sum,k)
    if array_sum > k and array_sum!=0:
        return array_sum
    else:
        return k


print(maxSubArraySumCircular([1,-2,3,-2]))
