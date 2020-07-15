def palindrome_permutation(string):
    char_count = {}
    for i in string:
        if i in char_count:
            char_count[i] +=1
        else:
            char_count[i] = 1

    chars_not_occuring_twice = 0

    for char in char_count:
        if char_count[char] %2 !=0:
            chars_not_occuring_twice +=1

    if chars_not_occuring_twice>1:
        return False
    else:
        return True

print(palindrome_permutation("aaab"))
