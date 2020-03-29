def minSteps(s,t):
    """
    https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
    """
    counter = 0
    temp = len(s)

    for i in t:
        if i in s:
            counter+=1
            t= t.replace(i,"",1)
            s= s.replace(i,"",1)
    return temp - counter

print(minSteps("anagram"
               ,"mangaar"))
