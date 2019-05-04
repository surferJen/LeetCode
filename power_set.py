# TEST:

# >>> []
# > [ [] ]

# >>> [1]
# > [ [], [1] ]

# >>> [1, 2]
# > [ [], [1], [2], [1, 2] ]

# >>> [1, 3, 4]
# > [ [], [1], [3], [4], [1, 3], [1, 4], [3, 4], [1, 3, 4] ]

# PSEUDO:
    # returns a set of sets
def create_power_set(inputSet):
        #set a variable n, which would equate to the len(set)
        
        #[1, 2, 3, 4, 5]
        #[2, 3, 4, 5] [1, 3, 4, 5] [1, 2, 4, 5] [1, 2, 3, 5] [1, 2, 3, 4]... -layer of lists with 4 items
        #[3, 4, 5] [2, 4, 5] [2, 3, 5] [2, 3, 4]... -layer of lists with 3 items
        #[4, 5] [3, 5] [3, 4]... -2 items
        #[4] [5]... -i item

        #[1, 2, 3, 4]
        #[1, 2, 3] [1, 2, 4] [1, 3, 4] [2, 3, 4]

        #[1, 3, 4]
        #[1, 3] [1, 4] [3, 4]
        #[1] [3] [1] [4] [3] [4]
        
        
        # [ [1,3,4] ]
        
        # create_power_set([3,4]) returns [[], [3], [4], [3,4]]

    if inputSet is None:
        return 
        
    result_set = set()
    result_set.add(frozenset(inputSet))

    for val in inputSet:
        copySet = inputSet.copy()
        copySet.remove(val)
        print(copySet)
        result_power_set = create_power_set(copySet)
        if (result_power_set is not None):
            result_set.union(result_power_set)
            
    return result_set
 
print(create_power_set({1, 2, 3, 4}))