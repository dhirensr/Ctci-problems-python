def minAddToMakeValid(S):
    """
    https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
    """
    stack = []
    for i in S:
        if(i=="("):
            stack.append(i)
        else:
            if(stack and stack[-1]=="("):
                stack.pop()
            else:
                stack.append(i)
    return len(stack)

print(minAddToMakeValid("((("))
