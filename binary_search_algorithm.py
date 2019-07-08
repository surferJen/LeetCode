#INTERVIEW CAKE

def binary_search(target, nums):
    """See if target appears in nums"""

    floor_index = -1
    ceiling_index = len(nums)

    while floor_index + 1 < ceiling_index:

        distance = ceiling_index - floor_index
        half_distance = distance // 2
        guess_index = floor_index + half_distance

        guess_value = nums[guess_index]

        if guess_value == target:
            return True
        
        if guess_value > target: 
            ceiling_index = guess_index
        
        else:
            floor_index = guess_index
        
        return False 

binary_search(3, [4, 5, 6, 2, 3, 6, 9, 0])
binary_search(3, [4, 5, 8, 2, 9, 9, 0, 2])