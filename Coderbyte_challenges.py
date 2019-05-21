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
        







    
    