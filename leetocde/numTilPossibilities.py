from collections import Counter
"""
 a very naive and dirty solution
could have done better with using factorial mathematical trick
"""
dict = {}

def helper(length,tiles):
    if(length == 1):
        dict[length] = [i for i in tiles]
    else:
        temp_list = []
        unique_chars = set([i for i in tiles])
        previous_elements = dict[length-1]
        for j in previous_elements:
            for k in unique_chars:
                not_add = False
                temp = Counter(str(j+k))
                for l in temp:
                    if(temp[l] > Counter(tiles)[l]):
                        not_add = True
                        break
                if (not_add ==False):
                    temp_list.append(j+k)
        dict[length] = temp_list



def numTilePossibilities(tiles):
    """
    https://leetcode.com/problems/letter-tile-possibilities/
    """
    for i in range(1,len(tiles)+1):
        helper(i,tiles)
    counter = 0
    for i in dict:
        temp = len(set(dict[i]))
        counter+= temp
    return counter

print(numTilePossibilities("aaabbc"))
