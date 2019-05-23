# CHALLENGE 1

# Have the function LetterChanges(str) take the str parameter being passed and modify it using the following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. 

# Sample Test Cases

# Input:"hello*3"

# Output:Ifmmp*3


# Input:"fun times!"

# Output:gvO Ujnft!

def LetterChanges(str):
    
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    vowels = ["a", "e", "i", "o", "u"]

    answer_lst = []

    for char in str:
        if char in alphabet: 
            answer_lst.append(alphabet[alphabet.index(char) + 1])
        else:
            answer_lst.append(char)
    
    for item in answer_lst:
        if item in vowels:
            answer_lst[answer_lst.index(item)] = item.upper()

    answer = "".join(answer_lst)
    return answer

print(LetterChanges("fun times!"))
print(LetterChanges("hello*3"))

#CHALLENGE 2