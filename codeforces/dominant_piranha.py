def dominant_piranha(piranhas):
    index = -1
    max_element = max(piranhas)
    for i in range(len(piranhas)):
        if piranhas[i]==max_element:
            if (i>0 and piranhas[i-1]< max_element) or (i<len(piranhas)-1 and piranhas[i+1]<max_element):
                index = i+1
                break
    return index


t = int(input())
for i in range(t):
    n = int(input())
    piranhas = [int(x) for x in input().split()]
    print(dominant_piranha(piranhas))
