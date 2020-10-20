def boring_apartments(num):
    digits_pressed = 0
    for i in range(1,int(str(num)[0])):
        digits_pressed = digits_pressed +10

    for i in range(1,len(str(num))+1):
        digits_pressed +=i
    return digits_pressed


t = int(input())
for i in range(t):
    n = int(input())
    print(boring_apartments(n))
