def subtractProductAndSum(n):
    """
    https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
    """
    digits_list = [int(i) for i in str(n)]
    sum_of_digits = 0
    product_of_digits = 1
    for i in digits_list:
        sum_of_digits  = sum_of_digits + i
        product_of_digits = product_of_digits * i
    return product_of_digits - sum_of_digits

print(subtractProductAndSum(234))
