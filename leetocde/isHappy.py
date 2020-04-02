def isHappy(n):
    cache = []
    while (n!=1 and n not in cache):
        split_n = [int(i) for i in str(n)]
        cache.append(n)
        n = 0
        for i in split_n:
            n+= i*i
    if(n==1):
        return True
    if (n in cache):
        return False
print(isHappy(19))
