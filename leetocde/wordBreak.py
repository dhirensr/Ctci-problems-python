def wordBreak(s,wordDict):
    stack = [s]
    seen = set()
    while stack:
        x = stack.pop()
        for i in wordDict:
            if x == i:
                return True
            l = len(i)
            if x[:l] == i and x[l:] not in seen:
                seen.add(x[l:])
                stack.append(x[l:])
    return False
print(wordBreak("catsandog",
["cats","dog","sand","and","cat"]
))
