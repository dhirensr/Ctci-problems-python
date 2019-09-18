#time complexity wise slow but correct algo
def helper_sequence(sequences,array):
    temp_sequences=[]
    for i in sequences:
        for j in array:
            if(j not in i):
                if(i+(j,) not in temp_sequences and (j,)+i not in temp_sequences):
                    temp_sequences.append(i+(j,))
    return temp_sequences

def sequence(array,k=1):
    temp=[]
    all_sequences=[]
    for i in array:
        if((i,) not in temp):
            temp.append((i,))
    if k==0:
        all_sequences=all_sequences+temp
    for i in range(k):
        sequences=helper_sequence(temp,array)
        temp=sequences
        if (k-1==i):
            all_sequences=all_sequences+sequences
    min_sum=min([sum(i) for i in all_sequences])
    count=0
    for i in all_sequences:
        if(sum(i)==min_sum):
            count+=1
    return count

t=int(input())

while(t>0):
    t-=1
    n,k=input().split()
    array=[int(i) for i in input().split()]
    print(sequence(array,int(k)-1))
