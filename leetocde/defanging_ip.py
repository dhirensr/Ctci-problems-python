def defangIPaddr(address):
    result=""
    for i in address:
        if(i=="."):
            result+="[.]"
        else:
            result+=i
    return result
