# Suppose we had a list ↴ of nn integers sorted in ascending order. How quickly could we check if a given integer is in the list?

#num = 7
#lst = [2, 3, 4, 5, 6, 7]

def find_integer_in_array(num, lst):
    floor_index = -1
    ceiling_index = len(lst)

    while floor_index + 1 < ceiling_index:
        distance = ceiling_index - floor_index

