# define count and say
# 1 , output would be 11
# 11, output would be 21
# 21, outputwould be 1211
# 1211, output would be 111221

# PSEUDOCODE:
# iterating over the digits. the numbers i keep track of is numbers 1-9. i check to see how many times the numbers repeat themselves until a different number appears. there must be a counter to check for the repetition of numbers. once there is a change in number, then iterator starts again to account for different number. before the reiteration occurs, i want to push the counter number and the number that is counted into a list. in the end i will join that list into a string.

# CODE:
# num = 12
# def count_numbers(num):
#     new_list = []
#     num = str(num)

#     counter = 0
#     previous_value = 0
#     for index, value in enumerate(num):
#         if index == 0:
#             counter += 1
#         if index != 0:
#             previous_value = num[index - 1]
#         if value == previous_value:
#             counter += 1
#         if value != previous_value:
#             new_list.append(counter)
#             counter = 0
#             previous_value = int(previous_value)
#             new_list.append(previous_value)
        
    
#     # new_string = "".join(new_list)
#     return new_list

# print(count_numbers(112))

def count_numbers(num):
    
    new_list = []
    num = str(num)
    counter = 0

    current_value = 0
    
    for value in num:
        if current_value == 0:
            current_value = value
            counter += 1
        elif current_value == value:
            counter += 1
    
        elif value != current_value:
            new_list.append(counter)
            counter = 0
            new_list.append(current_value)
            counter += 1
            current_value = value
    
    new_list.append(counter)
    new_list.append(current_value)
        

    return new_list

print(count_numbers(112233))
             
