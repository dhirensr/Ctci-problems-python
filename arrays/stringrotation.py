x='waterbottle'
y='eqbottlewat'
#this problem assumes both strings x and y of equal length
#just checking if string is rotable or not

def is_substring(x,y):
    for i in x:
        if i in y:
            y=y.replace(i," ",1)
        else:
            return False
    return True


print(is_substring(y,x))
