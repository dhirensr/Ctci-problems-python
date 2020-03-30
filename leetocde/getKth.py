def get_powers(number):
    result = []
    while number!=1:
        if(number%2 ==0):
            temp = number//2
            result.append(temp)
        else:
            temp = 3 *number +1
            result.append(temp)
        number = temp
    return result


def getKth(lo,hi,k):
    """
    https://leetcode.com/problems/sort-integers-by-the-power-value/
    """
    power_list = []
    for i in range(lo,hi+1):
        power_list.append([i,len(get_powers(i))])
    power_list.sort(key=lambda x: x[1])
    val,power = power_list[k-1]
    return val

print(getKth(7,11,4))
