def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def groupThePeople(groupSizes):
    """
    https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
    """
    distinct_groups = set(groupSizes)
    groups = max(groupSizes)
    occurences = [[] for i in range(groups+1)]
    output = []
    extra_groups = {}
    for idx,i in enumerate(groupSizes):
        if i not in extra_groups:
            extra_groups[i] = []
        extra_groups[i].append(idx)

    for key in extra_groups:
        if(len(extra_groups[key]) != key):
            temp = list(chunks(extra_groups[key],key))
            output = output + temp
        else:
            output.append(extra_groups[key])
    return output

print(groupThePeople([2,1,3,3,3,2]))
