def reverse(x):
    """
    https://leetcode.com/problems/reverse-integer/
    """
    if(x >= 0):
        reverse = "".join(str(x)[::-1])
        output = int(reverse)
    else:
        reverse = "".join(str(x)[1::][::-1])
        output =  -1*int(reverse)
    if(output< -1*2**31 or output > (2**31-1)):
        return 0
    else:
        return output

print(reverse(1534236469))
