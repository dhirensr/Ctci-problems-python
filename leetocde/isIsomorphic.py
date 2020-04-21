def isIsomorphic(s,t):
    _map = {}
    for i,j in zip(s,t):
        if i in _map:
            if j != _map[i]:
                return False
        else:
            if j not in _map.values():
                _map[i] = j
            else:
                return False
    return True


print(isIsomorphic('a','a'))
