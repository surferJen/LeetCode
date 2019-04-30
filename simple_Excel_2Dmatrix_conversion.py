# In:

# 2D matrix
# =A1 where A indexes into the column and 1 indexes into the row
# =(column index, row index)
# =A1 is essentially m[0][0]
# Values in the spreadsheet only ever be:
# - Integers
# - References in the form above

# [
#   [1, 4, =A1, =A2]
# ]

# [
#   [1, 4, (0, 0), (1, 0)] # zero-indexed
# ]

# Output: [
# 	[1,4,1,4]
# ]

# [
#   [1, 4, 1, #REF?] # zero-indexed
# ]

# [
#   [2, 4, 6]
#   [5, 3, 6]
#   [3, 5, 3]
# ]

# [ 
#   [A1, B1, C1],
#   [A2, B2, C2],
#   [A3, B3, C3]
# ]

# Out:

# # Values resolved
# [
#   [1, 1]
# ]

# [
#   [2, 4, 6]
#   [5, 3, 6]
# ]

# PSEUDO:
#  #check every (iterate) list within the list
# #iterate over every value inside list within list
# #{ 1: [...]

# 2: [....]
# }
# #query into key. Iterate over those values and if they are numbers, just print them out. If they are a reference, then grab the value that is equal to the reference.

# [
#   [1, 2, 3]
#   [1, C1]
# ]

# M[1][0] = 1
# M[0][0] = 1
# M[0][1] = 2

# =A1 -> (0, 0)
# …
# Cell = M[0][0]
# B1
# C1

Def resolve_reference(reference_string):
	# reference_string is a string like “=A1”, “=B2”, etc.
	list_of_alphabets = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R,
    S, T, U, V, W, X, Y, Z]

    Reference_string = reference_string[1,]

    Return (Indexof[Reference_string[0]], Reference_string[1])
		
		

	# returns a tuple in (r, c) form, where:
    # r is the row index denoted by the number component and 
    # c is the column index denoted by the letter component




Def generate_values(input_matrix):

    output_matrix = []
    For row in input_matrix:
        Intermediate_row = []
	For value in row:
		If value is not an int:
			r, c = resolve_reference(value)
            Intermediate_row.append(input_matrix[r][c-1])
        else: 	
            Intermediate_row.append(value)
	        output_matrix.append(Intermediate_row)
    Return output_matrix

# Scratch:

# =AA1
# =B100000

# Questions:

# Are all letters going to be capitalized?

