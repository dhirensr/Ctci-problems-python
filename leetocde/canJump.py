
vals=[]
def helper(nums,index):
    value=False
    if index >= len(nums):
        value= True
    elif nums[index] >= len(nums):
        value= True
    elif index== len(nums)-1:
        value = True
    else:
        for i in range(1,nums[index]+1):
            value = helper(nums,index+i)
    vals.append(value)
    return value

def canJump(nums):
    helper(nums,0)
    print(vals)


def canJump2(nums):
    lastgoodposition= len(nums)-1
    for i in range(lastgoodposition,-1,-1):
        if i+nums[i]>=lastgoodposition:
            lastgoodposition=i
            print(lastgoodposition)
    return lastgoodposition==0


print(canJump2([2,3,1,1,4]))
