#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.


name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
lst = list()
counts = dict()



for lines in handle:
    words = lines.split()
    i=0    
    for word in words:    
        if i < len(words) and words[i] == "From":
            hsplit = words[5].split(":")
            hsplit = hsplit[0]
            counts[hsplit] = counts.get(hsplit,0) + 1
        i=i+1


for h,c in counts.items():
    newtup = (h,c)
    lst.append(newtup)

lst = sorted(lst)

for x,y in lst:
    print(x,y)