left_brackets=['{','(','[']
right_to_left={'}':'{',']': '[',')':'('}

def paranthesis_checker(input_str):
    stack=[]
    for char in input_str:
        if char in left_brackets:
            stack.append(char)
        elif not stack or stack.pop() != right_to_left[char]:
            return False
    if stack:
        return False
    return True

print(paranthesis_checker('{{{[}}}'))
