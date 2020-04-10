output= []
def helper(current_ans,opened,closed,n):
    if(len(current_ans) == 2*n):
        output.append(current_ans)
        return
    if(opened < n):
        helper(current_ans+"(",opened+1,closed,n)
    if (closed < opened):
        helper(current_ans+")",opened,closed+1,n)


def generateParanthesis(n):
    helper("",0,0,n)
    return output

generateParanthesis(3)
