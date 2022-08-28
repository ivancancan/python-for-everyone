uservalue = input("Type a number")

try :
    inumber = int(uservalue)
except:
    inumber = -1

if inumber > 0:
    print("This is a number")
else:
    print("Not a number")