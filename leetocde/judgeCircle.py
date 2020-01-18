def judgeCircle(moves):
    point=[0,0]
    for i in moves:
        if(i=='U'):
            point[1]+=1
        elif(i=='D'):
            point[1]-=1
        elif(i=='L'):
            point[0]-=1
        else:
            point[0]+=1
    if(point[0]==0 and point[1]==0):
        return True
    else:
        return False


print(judgeCircle("LL"))
