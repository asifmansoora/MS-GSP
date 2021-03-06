
import re


from collections import Counter

# Function for flattening lists of list
def Listflat(Mainlist):
    for itemset in Mainlist:
        if type(itemset) in (list, tuple):
            for item in Listflat(itemset):
                yield item
        else:
            yield itemset
# More easier line : list(itertools.chain(*strippedSeqItem))

# Reading the transaction file
#Filename = '/Users/asifmansoor/MS-GSP/Data/data.txt'
Filename="C:\\Users\\balachandar\\Desktop\\Study\\Fall_2013\\Projects\\DM\\MSGSP\\data.txt"
openFile = open(Filename)
contents = openFile.read()

# Splitting each line with delim 
withline = contents.split("\n")
N = len(withline) - 1 # Total Number of transactions, eliminating the last null transaction


# Extracting the numbers alone with reg ex and appending it to a list
strippedSeqItem =[]

for line in withline:
    ItemList = re.sub(r'\D'," ",line).strip()
    
    strippedSeqItem.append(ItemList.split())


# A list containing all the items in the transaction, with orders preserverd
strippedSeq=[]

#Removing the duplicates and storing in another list to get count an item only once per transaction
for l in strippedSeqItem:
    strippedSeq.append(list(set(list(l))))
    

itemsAll = list(Listflat(strippedSeq))


# Use counter data structure to hold all the items with its count values
countItems = Counter(itemsAll)
#print countItems


