def msbPos(n):
    msb_p=-1
    while n>0:
        n = n>>1
        msb_p+=1
    return msb_p

def rangeBitwiseAnd(m,n):
    result=0
    while(m >0 and n>0):
        msb_p_m = msbPos(m)
        msb_p_n = msbPos(n)
        if(msb_p_n != msb_p_m):
            break
        result += 2*msb_p_m

        m = m- 2**msb_p_m
        n = n - 2**msb_p_n
    return result
