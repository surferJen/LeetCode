#You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

#Write a function get_products_of_all_except_at_index() that takes a list of integers and returns a list of the products

#Testcase:
# [1, 7, 3, 4]
#     >>>[84, 12,  28, 21]

#by calculating: [7*3*4, 1*3*4, 1*7*4, 1*7*3]

[1, 1, 7, 21]

def get_products_of_all_except_at_index(list_of_nums):
    
    list_of_products = [None] * len(list_of_nums)
    product_of_nums = 1

    for i in range(len(list_of_nums)):
        list_of_products[i] = product_of_nums
        product_of_nums *= list_of_nums[i]
    
    product_of_nums = 1
    for i in range(len(list_of_nums)-1, -1, -1):
        list_of_products[i] *= product_of_nums
        product_of_nums *= list_of_nums[i]

    return list_of_products


print(get_products_of_all_except_at_index([1, 7, 3, 4]))
        