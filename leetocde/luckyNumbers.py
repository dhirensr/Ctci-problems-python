def luckyNumbers (matrix):
    """
    https://leetcode.com/problems/lucky-numbers-in-a-matrix/
    """
    rows = [min(row) for row in matrix]

    cols = [max([row[i] for row in matrix]) for i in range(len(matrix[0]))]

    return [i for i in rows if i in cols]

print(luckyNumbers([[3,7,8],[9,11,13],[15,16,17]]))
