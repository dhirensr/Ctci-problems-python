def generateTheString(n):
    output = ""
    if(n%2==0):
        output += 'a'*(n-1)
        output += 'b'*1
    else:
        output += 'a'*n
    return output

print(generateTheString(7))
