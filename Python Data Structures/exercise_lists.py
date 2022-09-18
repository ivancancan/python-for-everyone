#Open the file romeo.txt and read it line by line. For each line, split the line into a 
#list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
#When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
#You can download the sample data at http://www.py4e.com/code3/romeo.txt

    #split = line.split()
    #split.sort()
    #len()
    #stuff.append(thing)
    # "something" in variable

fname = input("Tell me the file name: ")
fh = open(fname)
lst = list()

for line in fh:
    vsplit = line.split()
    i = 0
    for words in vsplit:
        #print(vsplit[i])
        if vsplit[i] not in lst:
            lst.append(vsplit[i])
        i = i + 1
        
lst.sort()            
print(lst)    

