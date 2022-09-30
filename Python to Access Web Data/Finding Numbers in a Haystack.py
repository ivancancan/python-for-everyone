import re
#import regular expressions since it is not by default in python
#re.search () returns a True or False
#re.findall() returns matching strings and extract them.



fname = input("File Name: ")
if len(fname) < 1:
    fname = "regex_sum_42.txt"

fh = open(fname)

numlist = list()

for lines in fh:
    lines = lines.rstrip()
    y = re.findall('[0-9]+', lines)
    if len(y) < 1 : continue
    else:
        for numbers in y:
            numlist.append(int(numbers))

Sum = sum(numlist)

print(Sum)