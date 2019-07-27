def check_larger_element(stack,element):
    while(stack):
        temp=stack.pop()
        if(temp>element):
            result=temp
            return result
    return -1

def next_larger_element(array):
    results=[]
    for idx, i in enumerate(array):
        stack=array[idx:][::-1]
        results.append(check_larger_element(stack,i))
    return results

print(next_larger_element([4,3,2,1]))
