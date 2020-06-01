def removeKdigits(num, k):
    possible_values=[]
    less_digits = len(num)-k
    if less_digits ==0:
        return "0"
    # def helper(num,i,j,less_digits):
    #     temp = num[:i] + num[j+1:]
    #     temp1= num[i:i+less_digits]
    #     possible_values.append(int(temp))
    #     if len(temp1) == less_digits:
    #         possible_values.append(int(temp1))

    # for i in range(less_digits+1):
    #     helper(num,i,i+k-1,less_digits)
    # print(possible_values)

    # result=str(min(possible_values))
    # return result
    stack = []
    pop_count=0
    for i in num:
        val = int(i)
        while pop_count!=k and stack and stack[-1] > val:
            stack.pop()
            pop_count+=1
        stack.append(val)

    answer= "".join(str(v) for v in stack[0:less_digits]).lstrip("0")
    return answer


print(removeKdigits("112",1))
