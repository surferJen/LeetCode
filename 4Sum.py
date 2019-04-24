class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # create a new list called ans
        # find four numbers in the given list that sums up to the target value
        # *I have to check for every possible value.
        # *how do i check for duplicates? create a set
        # if that list does not exist in ans, then append to ans
        
        
        a = 0
        b = 1
        c = 2
        d = 3
    
        ans = []
       
        while a < len(new_list):
            
            while b < len(new_list):
                
                while c < len(new_list):
                    
                    while d < len(new_list):
                
                        if new_list[a] + new_list[b] + new_list[c] == target:
                            ans.extend([new_list[a], new_list[b], new_list[c]])
                        
                        d+=1
                
                    c += 1
                    d = c + 1
                
                b += 1
                c = b + 1
                d = c + 1
            a +=1
            b = a + 1
            c = b + 1
            d = c + 1
            

        new_ans = set(ans)
        return new_ans