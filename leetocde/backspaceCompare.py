def backspaceCompare(S,T):
    s_result=""
    t_result=""
    for i in S:
        if(i == "#"):
            s_result = s_result[:-1]
        else:
            s_result+=i
    for i in T:
        if(i == "#"):
            t_result = t_result[:-1]
        else:
            t_result+=i
    return s_result == t_result


print(backspaceCompare("ab#","c"))
