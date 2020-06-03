def char_count(s):
    value_dict= {}
    for i in s:
        if i in value_dict:
            value_dict[i]+=1
        else:
            value_dict[i] = 1
    return value_dict

def findAnagrams(s,p):
    unique_chars = char_count(p)
    #print(unique_chars)
    result=[]
    for i in range(len(s)):
        temp = s[i:i+len(p)]
        #print(temp)
        if set(temp) == set(p) and len(temp) ==len(p):
            if char_count(temp) == char_count(p):
            #print(char_count(temp), unique_chars)
                result.append(i)
    print(result)
    return result

findAnagrams("ababababab","aab")

#print(char_count("aa"))
