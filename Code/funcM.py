'''
Created on Sep 16, 2013

@author: asifmansoor
'''
from __future__ import division
from LSeed import countItems,N
import sys


    
def main():
    
    MIS={}
    M=[]
    L=[] # L-seed list
    #FILE_LOC="C:\\Users\\balachandar\\Desktop\\Study\\Fall_2013\\Projects\\DM\\MSGSP\\para.txt"
    FILE_LOC="para.txt"

    
    for line in open(FILE_LOC,"r"):
        if(("SDC" or "sdc")  not in line):
            key=int(line[line.find("(")+1:line.find(")")])
            value=float(line[line.find("=")+1:].strip("\n"))
            MIS[key]=value
    
       
    M=sort(MIS,M)
    
    
#     print M
#     print MIS
    
    # Check the first index element which satisfies MIS(i)
    itemCtr =0
    for item in M:
        if (countItems.get(str(item))/N < MIS.get(item) ):
            itemCtr = itemCtr+1;
        else:
            break
    
#     print itemCtr
        
    # Appending the first item to L-seed
    firstItem = M[itemCtr]
    firstItemMIS = MIS.get(firstItem) 
    L.append(firstItem)
    
    # Searching the element after first item which satisfies the
    # MIS(i) value
    for item in M[itemCtr+1:]:
        if (countItems.get(str(item))/N >= firstItemMIS ):
            L.append(item)
    
    print L  
    
    f1GenSet(L,MIS)
#     To check all the items in countItems dataset
#     intvalu = []
#     for value in countItems.keys():
#         intvalu.append(int(value))
#         
#     print intvalu.sort()

            #print line[line.find("(")+1:line.find(")")],line[line.find("=")+1:]
def f1GenSet(LSeed,MIS):
    f1=[]
    for item in LSeed:
        if (countItems.get(str(item))/N >= MIS.get(item) ):
            f1.append(item)
            
    print f1    

def sort(MIS,M):
       
    for i in sorted(MIS, key=MIS.get, reverse=False) :
        M.append(i)
  
     
     
    return M
    
  
    
if  __name__ =='__main__':main()