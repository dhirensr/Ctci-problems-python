def checkValidString(s):
    stack = []
    stack_star = []
    for idx,i in enumerate(s):
        if i=="(":
            stack.append(idx)
        if i== ")":
            if stack:
                stack.pop()
            elif stack_star:
                stack_star.pop()
            else:
                return False
        if i=="*":
            stack_star.append(idx)
    print(stack,temp)
    while stack and stack_star:
        if stack[-1] < stack_star[-1]:
            stack.pop()
            stack_star.pop()
        else:
            break
    return len(stack) ==0

print(checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*"))
