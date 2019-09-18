fibonacci_elements={0:0,1:1}
def fibonacci(N_elements):
    if N_elements-1 not in fibonacci_elements and (N_elements>1):
        for i in range(2,N_elements):
            fibonacci_elements[i]=fibonacci_elements[i-1]+fibonacci_elements[i-2]
    return [fibonacci_elements[i] for i in range(N_elements)]

def helper(fib_seq):
    temp=[]
    if(len(fib_seq)==1):
        return fib_seq[0]
    else:
        for i in range(1,len(fib_seq),2):
            temp.append(fib_seq[i])
        return helper(temp)

def easy_fibonacci(number):
    fib_seq=fibonacci(number)
    print(helper(fib_seq)%10)

t=int(input())
while(t>0):
    t-=1
    number=int(input())
    easy_fibonacci(number)
