def juggling_letters(n,strings):
    char_count = {}
    for string in strings:
        for char in string:
            if char in char_count:
                char_count[char] +=1
            else:
                char_count[char] = 1

    for char in char_count:
        if char_count[char]%n !=0:
            return "NO"
    return "YES"


T=int(input())
for i in range(T):
    strings = []
    n = int(input())
    for i in range(n):
        strings.append(input())
    print(juggling_letters(n,strings))
