def maximum69Number (num):
    '''
    https://leetcode.com/problems/maximum-69-number/
    '''
    temp = str(num)
    temp = temp.replace('6', '9',1)
    return int(temp)
print(maximum69Number(9999))
