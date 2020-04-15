def stringShift(s,shift):
    for i,j in shift:
        if i==0 and j>0:
            s= s[j:]+ s[:j]
        if i ==1 and j>0:
            s = s[-j:]+ s[:len(s)-j]
    return s

print(stringShift("joiazl",
[[1,1],[1,6],[0,1],[1,3],[1,0],[0,3]]))
