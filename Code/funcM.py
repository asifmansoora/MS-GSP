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
        else:
          sdc=float(line[line.find("=")+1:].strip("\n"))
    
       
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
    

    
    f1GenSet(L,MIS)
    
    #Converting L list  into String:
    for i in range(0,len(L)):
        L[i]=str(L[i])
     
    #Converting MIS dictionary into String: 
    for key,value in MIS.iteritems():
        del MIS[key]
        MIS[str(key)]=value
        
    
    # 'C' is Candidate List 
    C=level2candgen(L,MIS,countItems)
    #print(len(C))

    
    
    
    
    
    
#     To check all the items in countItems dataset
#     intvalu = []
#     for value in countItems.keys():
#         intvalu.append(int(value))
#         
#     print intvalu.sort()

            #print line[line.find("(")+1:line.find(")")],line[line.find("=")+1:]



def level2candgen(L,MIS,countItems):
    C=[]
    for l in range(0,len(L)):
        #print "I:",L[l],"C:",(countItems[L[l]])*0.014,"M:",MIS[L[l]]
        if float(countItems[L[l]])/float(N) >= MIS[L[l]]:
                    
            
            for h in range(l+1,len(L)):
                if countItems[L[h]]*0.014 >= MIS[L[l]] and abs(countItems[L[h]]*0.014-MIS[L[l]]) <= 0.05:
                    str1="{"+L[l]+","+L[h]+"}"
                    C.append(str1)
                    str2="{"+L[l]+"}"+"{"+L[h]+"}"
                    C.append(str2)
    
    return C

    


def f1GenSet(LSeed,MIS):
    f1=[]
    for item in LSeed:
        if (countItems.get(str(item))/N >= MIS.get(item) ):
            f1.append(item)
            
    print "F1:",f1    

def sort(MIS,M):
       
    for i in sorted(MIS, key=MIS.get, reverse=False) :
        M.append(i)
  
     
     
    return M
    
  
    
if  __name__ =='__main__':main()