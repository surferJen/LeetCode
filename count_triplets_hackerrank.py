def countTriplets(arr, r)
    new_list = []
    for i in arr:
        if i % r == 0:
            new_list.append(i)
    x = len(new_list)



print(countTriplets([1, 4, 16, 64], 4) #2
print(countTriplets([2, 6, 18, 13], 3) #1

