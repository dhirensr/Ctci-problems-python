x='bake'
y='pale'
#assumption y is always bigger string
counter=0

for i in y:
    if(i in x):
        x=x.replace(i,' ',1)
    else:
        counter+=1
    if(counter>1):
        print('false')
        break
if(counter<=1):
    print('true')
