"""
TESTCASES:
    
    >>> "[]()"
    >True
    
    >>>"([])"
    >True
    
    >>> "{}[["
    >False
REQ:
    #What qualifies a valid input is if any new parentheses starts with (, [, { and always closes with the closed version of whatever it started with.

PSEUDO:
    
    #it checks to see if [, {, ( 
    # before {, }, ). and cannot start with }, ], ) without open equivalent open parens. 
    
    #create counter for parens
    #if }, ], ) > [ { (, you know that there is an unbalanced parens.  

"""

# FAIL:
#     ({})
#     ({)}  
#    (({))} you don't ever want an open parens in between two of the same open/close parens

#                  "({[{[]]"
 # "parens = ["(", "{", "[", "{", "["]       ] ]
     
    #"()"
class Solution:
    def isValid(self, s: str) -> bool:

        parens = []

        for i in s:
            if i in "[{(":
                parens.append(i)
            
            if parens == [] and i in "]})":
                return False
            
            if i in "]})":
                if i == ")" and parens.pop() != "(":
                    return False
                if i == "]" and parens.pop() != "[":
                    return False
                if i == "}" and parens.pop() != "{":
                    return False
        return True
    
