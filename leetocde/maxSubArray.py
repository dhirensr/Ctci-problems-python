
def maxCrossingSum(arr, l, m, h) :
    sm = 0
    left_sum = -10000
    for i in range(m, l-1, -1) :
        sm = sm + arr[i]
        if (sm > left_sum) :
            left_sum = sm
    sm = 0
    right_sum = -1000
    for i in range(m + 1, h + 1) :
        sm = sm + arr[i]
        if (sm > right_sum) :
            right_sum = sm
    return left_sum + right_sum;

def maxSubArraySum(arr, l, h) :
    # Base Case: Only one element
    if (l == h) :
        return arr[l]
    # Find middle point
    m = (l + h) // 2
    # Return maximum of following three possible cases
    # a) Maximum subarray sum in left half
    # b) Maximum subarray sum in right half
    # c) Maximum subarray sum such that the
    return max(maxSubArraySum(arr, l, m),
               maxSubArraySum(arr, m+1, h),
               maxCrossingSum(arr, l, m, h))
