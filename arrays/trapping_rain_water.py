def trapping_rain_water(array):
    """
    related to https://practice.geeksforgeeks.org/problems/trapping-rain-water/0
    """
    temp=array[0] # the wall of the rain water
    count=0
    for i in array[1:]:
        if(i> temp):
            return count
        else:
            count+=temp-i
    return count

print(trapping_rain_water([6,9,9]))
