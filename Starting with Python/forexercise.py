# 5.2 Write a program that repeatedly prompts a user for integer numbers until 
# the user enters 'done'. Once 'done' is entered, 
# print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a 
# try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.
# Desired output Invalid input, Maximum is 10, Minimum is 2


largest = None
smallest = None
while True:
    num = input("Enter a number: ")


  
    # Finish program when user input is done

    if num == "done":
        break


    try:
       inum = int(num)

    except:
        inum = -1
        print("Invalid input")
        continue
        
        
    # Largest number logic

    if largest is None:
        largest = inum
    elif largest < inum:
        largest = inum

    # Smallest number logic
        
    if smallest is None:
        smallest = inum
    elif smallest > inum:
        smallest = inum



print("Maximum is", largest)
print("Minimum is", smallest)



