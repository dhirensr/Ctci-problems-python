def freqAlphabets(s):
    output=""
    i=0
    while (i < len(s)):
        if(len(s)-i > 2 and s[i+2]=='#'):
            output+=chr(96+int(s[i:i+2]))
            i+=3
        else:
            output+=chr(96+int(s[i]))
            i+=1
        #print(output)

    return output


print(freqAlphabets('12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#'))
