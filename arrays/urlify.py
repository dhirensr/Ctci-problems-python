x='Mr John Smith           '
length=13
y=''
for i in range(length):
    if(x[i]==' '):
        y+='%20'
    else:
        y+=x[i]

print(y)
