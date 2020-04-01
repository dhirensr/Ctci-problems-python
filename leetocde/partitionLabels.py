def partitionLabels(S):
    """
    https://leetcode.com/problems/partition-labels/
    """
    last_dict = {}
    for idx,i in enumerate(S):
        last_dict[i] = idx
    split = []

    start =0
    end =0
    previous_count = 0
    for idx,i in enumerate(S):
        end = max(end,last_dict[i])
        if(idx == end):
            split.append(end-start+1)
            start = end+1
    return split


print(partitionLabels("qiejxqfnqceocmy"))
