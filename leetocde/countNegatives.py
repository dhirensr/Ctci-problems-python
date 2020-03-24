def countNegatives(grid):
    """
    https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
    """
    negative_count = 0
    for i in grid:
        for j in i:
            if(j < 0):
                negative_count+=1

    return negative_count

print(countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
