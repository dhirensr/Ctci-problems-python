def divide(dividend,divisor):
    divisor_abs= abs(divisor)
    dividend_abs = abs(dividend)
    count=0
    while dividend_abs >= divisor_abs and divisor_abs!=1:
        dividend_abs -= divisor_abs
        count+=1
    if divisor_abs==1:
        count = dividend_abs
    if (dividend<0 and divisor >0) or (dividend>0 and divisor <0):
        count = -count
    print(count)

    if -2**31 < count  and count < 2**31-1:
        return count
    else:
        return 2**31-1


def divide2(dividend,divisor):
    if (dividend<0 and divisor >0) or (dividend>0 and divisor <0):
        sign=-1
    else:
        sign =1
    dividend= abs(dividend)
    divisor = abs(divisor)
    quotient = 0
    temp = 0
    # test down from the highest
    # bit and accumulate the
    # tentative value for valid bit
    for i in range(31, -1, -1):
        #print(divisor<<i,i,)
        if (temp + (divisor << i) <= dividend):
            temp += divisor << i
            quotient |= 1 << i
    return sign * quotient


print(divide2(-2147483648,1))
