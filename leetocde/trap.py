def trap(height):
    """
    https://leetcode.com/problems/trapping-rain-water/
    """
    total = 0

    for i in range(1, len(arr)-1):
        l_max = max(arr[:i])
        r_max = max(arr[i+1:])
        diff  = min(l_max, r_max)
        if diff-arr[i] > 0:
            total = total + (diff-arr[i])

    return total


trap([0,1,0,2,1,0,1,3,2,1,2,1])
