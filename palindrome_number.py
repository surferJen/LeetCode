# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true

# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:

# Coud you solve it without converting the integer to a string?




# REQUIREMENTS:
# a negative number can not be a palindrome
# has to read the same reverse and forward

# PSEUDOCODE:
#     i am given an integer.
#     put it into a list, list_a
#     create a new list, list_b, with the reverse
#     if both lists are equal, return true. if not, return false
    

def isPalindrome(num):
        
    if num < 0:
        return False
        
    list_a = []
        
    while num >= 10:
        remainder = num % 10
        list_a.append(int(remainder))
        new_num = num - remainder
        new_new_num = new_num / 10
            
        if new_new_num < 10:
            list_a.append(int(new_new_num))
            
        num = new_new_num
        
    list_b = list_a[-1::-1]
    print(list_b)
        
    if list_a == list_b:
        return True
    else:
        return False

print(isPalindrome(-171))
print("_____^^^^^______")
print(isPalindrome(171))
print("_____^^^^^_____")
print(isPalindrome(456171))
print("___^^^^^^____")
print(isPalindrome(9))
print("____^^^^^^^____")
print(isPalindrome(88988))

# 5135 % 10 = 5
# 5135 - 5 = 5130
# 5130 / 10 = 513

# 513 % 10 = 3
# 513 - 3 = 510
# 510 / 10 = 51

# 51 % 10 = 1
# 51 - 1 = 50
# 50 / 10 = 5

# 5135 % 10 = 5
# 5135 % 100 = 35
# 5135 % 1000 = 135
# 5135 - 135 = 
# 5135 % 10000 = 5135


# 5135 % 100000 = 5135
# 5135 % 1000000 = 5135