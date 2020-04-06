

def groupAnagrams(strs):
    cache = {}
    result = []
    for idx,i in enumerate(strs):
        sorted_val = "".join(sorted(list(i)))
        if sorted_val in cache:
            cache[sorted_val].append(i)
        else:
            cache[sorted_val] = [i]
    for i in cache:
        result.append(cache[i])
    return result



print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
