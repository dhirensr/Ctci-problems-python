def reverse_array(array,start,num):
    end=len(array)-1
    swap_index=None
    swap_value=99999999999999
    while(start<=end):
        if(start<end):
            swap(array,start,end)
        if(array[end] > num and array[end] <=swap_value):
            swap_value=array[end]
            swap_index=end
        end-=1
        start+=1
    return swap_index

def swap(array,i,j):
    temp=array[i]
    array[i]=array[j]
    array[j]=temp


def next_permutation(array):
    i=len(array)-1
    while(array[i-1]>= array[i]):
        i-=1
    swap_index=reverse_array(array,i,array[i-1])
    if(swap_index!=None):
        swap(array,i-1,swap_index)
    return array

print(next_permutation([3,2,1]))
