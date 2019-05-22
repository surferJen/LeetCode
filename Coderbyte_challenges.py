#CHALLENGE 1

# Have the function FirstFactorial(num) take the num parameter being passed and return the factorial of it. For example: if num = 4, then your program should return (4 * 3 * 2 * 1) = 24. For the test cases, the range will be between 1 and 18 and the input will always be an integer. 

def FirstFactorial(num):
    
    if num == 1:
        return 1
    else:
        return num * FirstFactorial(num-1)

# print(FirstFactorial(3))
# print(FirstFactorial(5))
# print(FirstFactorial(10))

#CHALLENGE 2 Longest Word

# Have the function LongestWord(sen) take the sen parameter being passed and return the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume sen will not be empty. 

def LongestWord(sen):
    
    sen = sen.split(" ")
    
    current_count = 0
    max_count = 0
    answer = ""
    
    
    for i in sen:
        current_count = 0
        for x in i:
            if x.isalpha():
                current_count += 1

        if current_count > max_count:
            max_count = current_count
            answer = i  
    
    return answer
        
#CHALLENGE 3 REVERSE STRING


# Have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order. For example: if the input string is "Hello World and Coders" then your program should return the string sredoC dna dlroW olleH. 


# Sample Test Cases

# Input:"coderbyte"

# Output:etybredoc


# Input:"I Love Code"

# Output:edoC evoL I

def FirstReverse(str):

    
    reversed_str_lst = []
    answer = ""

    for index in range(len(str)-1, -1, -1):
        reversed_str_lst.append(str[index])
    
    answer = ''.join(reversed_str_lst)

    return answer


# print(FirstReverse("Jen loves programming"))
# print(FirstReverse("coderbyte"))
# print(FirstReverse("I Love Code"))

#CHALLENGE 4 REVERSE LIST

# Given an array of strings, reverse them and their order in such way that their length stays the same as the length of the original inputs.

'''
Test.assert_equals(
    reverse(["I", "like", "big", "butts", "and", "I", "cannot", "lie!"]),
            ["!", "eilt", "onn", "acIdn", "ast", "t", "ubgibe", "kilI"]
)

Test.assert_equals(
    reverse(["?kn", "ipnr", "utotst", "ra", "tsn", "iksr", "uo", "yer", "ofebta", "eote", "vahu", "oyodpm", "ir", "hsyn", "amwoH"]),
            ["How", "many", "shrimp", "do", "you", "have", "to", "eat", "before", "your", "skin", "starts", "to", "turn", "pink?"]
)
'''

# PSEUDO:
#     create an empty array.
#     append each character reversed by using reverse built in method. 
#     [a, s, d, f, g, s, ...]
#     iterate over input. count each string. and append that many chharacters to dictionary.

def ReverseLst(lst):
    
    new_input = "".join(lst)
    new_input = new_input[::-1]
    
    counter_lst = []
    
    counter = 0
    for i in lst:
        for x in i:
            counter += 1
        counter_lst.append(counter)
        counter = 0
    
    answer = []
    for y in counter_lst:
        
        answer.append(new_input[:y])
        new_input = new_input[y:]
    
    return answer
    
        

print(ReverseLst(["I", "like", "big"]))
print(ReverseLst(["I", "like", "big", "butts", "and", "I", "cannot", "lie!"]))
print(ReverseLst(["?kn", "ipnr", "utotst", "ra", "tsn", "iksr", "uo", "yer", "ofebta", "eote", "vahu", "oyodpm", "ir", "hsyn", "amwoH"]))

    





    
    