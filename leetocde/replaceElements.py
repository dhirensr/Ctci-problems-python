def replaceElements(arr):
    '''
     https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
     '''
    for idx,i in enumerate(arr[:-1]):
        print(arr[idx+1:])
        arr[idx] = max(arr[idx+1:])
    arr[-1] = -1
    return arr

print(replaceElements([17,18,5,4,6,1]))
