def queue_using_two_stacks(sequence):
    stack=[]
    popped_elements=[]
    ignore=None
    for idx,i in enumerate(sequence):
        if(i =='1'):
            ignore=1
            stack.append(int(sequence[idx+1]))
        elif(ignore):
            ignore=None
            pass
        elif(i=='2' and not ignore):
            if(stack):
                popped_elements.append(stack.pop(0))
            else:
                popped_elements.append(-1)
    return popped_elements


print(queue_using_two_stacks('122214'))
