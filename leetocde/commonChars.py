def commonChars(A):
    a = []
    for i in set(A[0]):
        a.extend([i]*min(j.count(i) for j in A))
    return a

print(commonChars(["bella","label","roller"]))
