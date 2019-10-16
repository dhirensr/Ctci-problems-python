
def balancedStringSplit(s):
    count=0
    temp_count=0
    for i in s:
        if(i=="L"):
            temp_count+=1
        else:
            temp_count-=1
        if(temp_count==0):
            count+=1
        return count

print(balancedStringSplit("RL"))
