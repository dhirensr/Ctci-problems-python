def numberOfSteps(num):
    """
    https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
    """
    counter = 0
    while(num!=0):
        if(num%2==0):
            num = num //2
            counter+=1
        else:
            num = num -1
            counter+=1
    return counter
print(numberOfSteps(123))
