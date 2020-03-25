def helper(s):
    return s[1:len(s)-1]

def removeOuterParentheses(S):
    """
    https://leetcode.com/problems/remove-outermost-parentheses/
    """
    temp = ""
    stack = []
    output = ""
    for i in S:
        if(i=="("):
            stack.append(i)
        elif(i==")" ):
            stack.pop()
        temp+=i
        if len(stack) ==0:
            output += helper(temp)
            temp = ""
    return output

print(removeOuterParentheses("(()())(())"))
