def swap(array,index_1,index_2):
    temp=array[index_1]
    array[index_1]=array[index_2]
    array[index_2]=temp
    return array


def sorting_array(array):
    '''
    related to https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s/0
    sort an array of 0's 1's and 2's
    '''

    for idx in range(len(array)-1):
        for j in range(idx,len(array)):
            if(array[idx] > array[j]):
                array=swap(array,idx,j)
    return array

print(sorting_array([0,1,0]))
