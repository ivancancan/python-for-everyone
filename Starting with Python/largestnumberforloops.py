largest_number_so_far = -1

print("Before", largest_number_so_far)

for the_num in [2, 41, 34, 12, 75, 20, 100, 20, 30] :
    if the_num > largest_number_so_far:
        largest_number_so_far = the_num
    print(largest_number_so_far, the_num)

print("After", largest_number_so_far)