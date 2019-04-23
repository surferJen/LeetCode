def letterCombinations(digits):
  # establish the letter equivalent to the number in a dictionary form
  # 1: None
  # 2: [a, b, c]
  # 3: [d, e, f]
  
  #cross check all possible letter combinations. iterating over the values of the dictionary
  
  digits_dict = { 1: None, 
                  2:["a", "b", "c"], 
                  3:["d", "e", "f"], 
                  4:["g", "h", "i"], 
                  5:["j", "k", "l"],
                  6:["m", "n", "o"], 
                  7:["p", "q", "r", "s"], 
                  8:["t", "u", "v"], 
                  9:["w", "x", "y", "z"], 
                  0: None}
  
  
  ans = []
      
  # outer for loop index
  i = 0
  # inner loop index
  j = 1

  while j < len(digits):
    num_values = digits_dict.get(int(digits[i]))
    second_values = digits_dict.get(int(digits[j]))
    if num_values is not None:
      #str_ans = ""
    # num_values = ["a", "b", "c"]
      for letter in num_values:
        # second_values = ["d", "e", "f"]
        for second_letter in second_values:
          ans.append(letter + second_letter)
          j = j + 1
        i += 1
  return ans
      

print(letterCombinations("23"))

#how to improve runtime