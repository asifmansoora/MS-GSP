'''
Created on Sep 16, 2013

@author: asifmansoor
'''
from __future__ import division
from collections import OrderedDict
from LSeed import countItems,N
import sys,re
import itertools

    
def main():
    
    MIS={}    # stores MIS values of all the items
    count={}  # Stores count of all the items
    M=[]      # Stores all the items in ascending order of their MIS
    F={}      #dictionary to store frequent Itemsets of all lengths
    L=[]      # Seed to generate C[2] and F[1]
    k=1       # main counter variable
    CandList = [] # List of all candidates
     # L-seed list
    #FILE_LOC="C:\\Users\\balachandar\\Desktop\\Study\\Fall_2013\\Projects\\DM\\MSGSP\\para.txt"
    FILE_LOC="para.txt"
    

    print "Started Running..."
    print "Reading parameter file.."
    for line in open(FILE_LOC,"r"):
        if(("SDC" or "sdc")  not in line):
            key=int(line[line.find("(")+1:line.find(")")])
            value=float(line[line.find("=")+1:].strip("\n"))
            MIS[key]=value
        else:
          sdc=float(line[line.find("=")+1:].strip("\n"))
    
    # sorts all items in ascending order of MIS   
    M=sort(MIS,M)
    print "Sorted M..."
    
    print "Generating L Seed...."
    # L Seed generation
    # Check the first index element which satisfies MIS(i)
    itemCtr =0
    for item in M:
        #print "here",countItems.get(str(item)),float(N),MIS.get(item),float(countItems.get(str(item)))/float(N)
        if (float(countItems.get(str(item)))/float(N) < MIS.get(item) ):
            
            itemCtr = itemCtr+1
        else:
            break
    
   # print itemCtr
        
    # Appending the first item to L-seed
    firstItem = M[itemCtr]
    firstItemMIS = MIS.get(firstItem) 
    L.append(firstItem)
    
    
    
    
    # Searching the element after first item which satisfies the
    # MIS(i) value
    for item in M[itemCtr+1:]:
        if (float(countItems.get(str(item)))/float(N) >= firstItemMIS ):
            L.append(item)
    
    
    
    
    
    
    
    print "F1 Generation....."
    #Generating F1
    f=f1GenSet(L,MIS)
    F[k]=[]
    for item in f:
        F[k].append("{"+str(item)+"}")
    
    k=k+1
    
    #Converting L list  into String format:
    for i in range(0,len(L)):
        L[i]=str(L[i])
        
    
     
    #Converting MIS dictionary into String format: 
    for key,value in MIS.iteritems():
        del MIS[key]
        MIS[str(key)]=value

    
    
    
    
    # Entering the main For Loop
    #print "Value of outer K is", k
    while (F[k-1]):
        #print "Value of K is", k
        if k==2:
            # Call candidate generation 2
            CandList = level2candgen(L,MIS,countItems,sdc)
            #print "Potential candidate 2 list",CandList
            
        else:
            # call candidate-k generation
            CandList = CandGen(F[k-1],MIS,k)
            #summa=0
        
        
        
            
        #Iterate through all the transactions with the generated Candidate 
       
        FILE_LOC="data.txt"
        for line in open(FILE_LOC,"r"):
            trans=line[line.find("<")+1:line.find(">")]
            #trans=trans.replace(" ","")
            for cand in CandList:
                #check=contains("{20,30}{80,90}","{10,20,30,70}{20,30,80}{45,90}{60,70,80}")
                cnt=0
                
                check=contains(cand,trans)
                #print "check",check
                # Count the presence of candidate in a transaction and store it in count
                if(check==1):
                    if cand not in count:
                        count[cand]=1
                    else:
                        count[cand]=count[cand]+1
                    #if k>=5:
                     #   print "count of K ",cand,count[cand]
                
        #print "Count",k,count
        
        F[k]=gen_F(CandList,MIS,count)
        print "Frequent Itemsets of sequence -",k ," are generated...."
        k=k+1
        
       
        
    #print "All Frequent Itemsets", F
    seqNum =1
    while(len(F)!=seqNum):
        print "The number of length ",seqNum, " Sequential patterns is ",len(F.get(seqNum))
        if(seqNum==1):
            for item in F.get(seqNum):
                print "Pattern: <",item,">  Count: ",countItems.get(item[item.find("{")+1:item.find("}")])
                
        else:
            for item in F.get(seqNum):
                print "Pattern: <",item,">  Count: ",count.get(item)
        
        print "******************************************************"
        print "                      "
        seqNum = seqNum+1
    
    
    #print "COunt :",count
    
    
    print "*************COMPLETED********************"
    #print confirmOrder("{30}{40}","{40}{30}{40, 60}")
   
  
        
    
#---------------------------- For loop ends here ----------------------------------------


#candidate Generation for F[k]
def CandGen(fkth,MIS,k):
    #print "Inside CanGen"
    
#     fkth = ['<{1},{4},{5}>','<{1},{4},{6}>','<{1},{5},{6}>','<{1},{5,6}>','<{1},{6},{3}>','<{6},{3},{6}>','<{5,6},{3}>','<{5},{4},{3}>','<{4},{5},{3}>']
    fKsplit =[]
    candList =[]

    for seq in fkth:
        fKsplit.append((seq.replace("<","")).replace(">",""))
#         print fKsplit


    for s1Seq in fKsplit:
        s1 = s1Seq
#         print "s1: ",s1

        for s2Seq in fKsplit:
            # s1 and s2 can be equal
            #if s1 == s2Seq:
                #print "s1=s2 :",s2Seq
                #continue

            
            s2 = s2Seq
            #print "s2 is different, s2 :",s2 
            
            listS1 = listItem(s1)
            listS2 = listItem(s2)
#             print listS1
            if(checkFirstItemLesser(listS1,MIS)==1):
                
            #check if the MIS Value of first item in s1 is smaller than 
            # the MIS value of all its item
            
                MISlastS2 = float(MIS.get(listS2[-1]))
                MISfirstS1 = float(MIS.get(listS1[0]))
                lastItemS1 = listS1[-1]
                lastItemS2 = listS2[-1]
                # remove 2nd item from listS1
                del listS1[1]
                # remove last item from listS2
                del listS2[-1]
    
#                 print "s1 :",(','.join(listS1))
#                 print "s2 :",(','.join(listS2))
#                     
#                 print "MIS last s2: ",MISlastS2
#                 print "MIS first s1: ",MISfirstS1
#                 print("LastItemS1 :", int(lastItemS1))
#                 print("LastItemS2 :", int(lastItemS2))
                if((','.join(listS1) == ','.join(listS2)) and (MISlastS2 > MISfirstS1)):
                    # append last item with '{' '}' to check for matching substring
                    lastElemS2 = "{"+lastItemS2 +"}"
#                     print "lastElemS2",lastElemS2 
                    
                    #check if the last item is an element in s2
                    if(s2.rfind(lastElemS2)==(len(s2)-len(lastElemS2))):
                        withLastElemS1=s1+lastElemS2
#                         print "c1 candidate :",withLastElemS1
                        candList.append(withLastElemS1)
                        if((lengthSeq(s1) == 2) and (sizeSeq(s1)==2) and (int(lastItemS2)>int(lastItemS1))):
                            lastElemItemS1 = s1[:len(s1)-1] +','+lastItemS2+s1[len(s1)-1:]
#                             print "c2 candidate :", lastElemItemS1
                            candList.append(lastElemItemS1)
                    
                    # else if the last item is not a separate element
                    
                    elif( ( (lengthSeq(s1)==2 and sizeSeq(s1)==1) and (int(lastItemS2)>int(lastItemS1))) or (lengthSeq(s1) >2)) :
                        ItemtoLastElemS1 = s1[:len(s1)-1] +','+lastItemS2+s1[len(s1)-1:]
#                         print "Item added to last element of S1: ", ItemtoLastElemS1
                        candList.append( ItemtoLastElemS1)
    
            elif(checkLastItemLesser(listS2,MIS)==1):
                
                #check if the MIS Value of first item in s1 is smaller than 
                # the MIS value of all its item
                MISlastS2 = float(MIS.get(listS2[-1]))
                MISfirstS1 = float(MIS.get(listS1[0]))
                firstItemS1 = listS1[0]
                firstItemS2 = listS2[0]
                # remove 1st item from listS1
                del listS1[0]
                # remove 2nd last item from listS2
                del listS2[-2]
    
#                 print "s1 :",(','.join(listS1))
#                 print "s2 :",(','.join(listS2))
#                     
#                 print "MIS last s2: ",MISlastS2
#                 print "MIS first s1: ",MISfirstS1
#                 print("LastItemS1 :", int(lastItemS1))
#                 print("LastItemS2 :", int(lastItemS2))
                if((','.join(listS1) == ','.join(listS2)) and (MISlastS2 < MISfirstS1)):
                    # append first item with '{' '}' in S1 to check for matching substring
                    firstElemS1 = "{"+firstItemS1 +"}"
#                     print "firstElemS1: ",firstElemS1 
                    #check if the First item is an first element in s1
                    if(s1.find(firstElemS1)==0):
                        withFirstElemS2=firstElemS1+s2
#                         print "c1 candidate :",withFirstElemS2
                        candList.append(withFirstElemS2)
                        if((lengthSeq(s2) == 2) and (sizeSeq(s2)==2) and (int(firstItemS1)<int(firstItemS2))):
                            firstElemItemS2 = s2[:1]+firstItemS1+','+s2[1:]
#                             print "c2 candidate :", firstElemItemS2
                            candList.append(firstElemItemS2)
                    
                    # if first item is not a separate element in s1
                    elif( ( (lengthSeq(s2)==2 and sizeSeq(s2)==1) and (int(firstItemS2)>int(firstItemS1))) or (lengthSeq(s2) >2)) :
                        ItemtoFirstElemS2 = s2[:1]+firstItemS1+','+s2[1:]
#                         print "Item added to first element of S2: ", ItemtoFirstElemS2 
                        candList.append( ItemtoFirstElemS2 )
            
            # Join using normal operation
            else:
                #print "here"
                candList.append((join(s1,s2)))
                candList=list(set(candList))    
                #candList.remove('')     
                 #print "After else :", candList
    # Print candidate list before pruning
    #print "Before Pruning",candList
    for i in range(0,len(candList)):
        if (prune(candList[i],fKsplit,MIS,k))==0:
            #print "Deleting Candidate",candList[i]
            del candList[i]
    
    
    #print "After Pruning",candList
    if '' in candList:
        candList.remove('')
    
    
    # Removes duplicates from the list
    candList=list(OrderedDict.fromkeys(candList))
    
    return candList        
    


    

#Generates F[k] from Candidate 'C'
def gen_F(C,MIS,count):
    
    C2=[]
    for c in C:
        items=re.findall(r'\d+',c)
        minitem=items[0]
        for item in items:
            if(MIS[item])<=MIS[minitem]:
                minitem=item
        
        
        if (c in count) and (float(count[c])/float(N)) >= MIS[minitem]:
            C2.append(c)
        #if (c in count) and (float(count[c])/float(N)) <= MIS[minitem]:
            #print "COunt",(float(count[c])/float(N)),"MIS:",MIS[minitem]
            
    return C2
    
        
        
    
#def join(s1,s2):



    
    
def level2candgen_b(L,MIS,countItems,sdc):
    #print "SDC",sdc
    C=[]
    #print "L:",L
    for l in range(0,len(L)):
        #print "I:",L[l],"C:",(countItems[L[l]])/float(N),"M:",MIS[L[l]]
        #if float(countItems[L[l]])/float(N) >= MIS[L[l]]:
            
                                
            for h in range(0,len(L)):
                #print "H:",L[h],"C:",(countItems[L[h]])/float(N),"M:",MIS[L[l]]
                if(h!=l):
                    min=l if MIS[L[l]]<=MIS[L[h]] else h                                                                  
                    if (countItems[L[h]]/float(N) >= MIS[L[l]] and abs((countItems[L[h]]/float(N))-(countItems[L[l]]/float(N)))<=sdc):
                        str1="{"+L[l]+","+L[h]+"}"
                        C.append(str1)
                        str2="{"+L[l]+"}"+"{"+L[h]+"}"
                        C.append(str2)
                        
    return C
    

# Modified the  logic to generate 2 item sets
def level2candgen(L,MIS,countItems,sdc):
    #print "SDC",sdc
    C=[]
    #print "L:",L
    for l in range(0,len(L)):
        #print "I:",L[l],"C:",(countItems[L[l]])/float(N),"M:",MIS[L[l]]
        #if float(countItems[L[l]])/float(N) >= MIS[L[l]]:
            
                                
            for h in range(l+1,len(L)):
                #print "H:",L[h],"C:",(countItems[L[h]])/float(N),"M:",MIS[L[l]]
                if(h!=l):
                                                                                    
                    if (countItems[L[h]]/float(N) >= MIS[L[l]] and abs((countItems[L[h]]/float(N))-(countItems[L[l]]/float(N)))<=sdc):
                        str1="{"+L[l]+","+L[h]+"}"
                        C.append(str1)
                        str2="{"+L[l]+"}"+"{"+L[h]+"}"
                        C.append(str2)
                        str3="{"+L[h]+","+L[l]+"}"
                        C.append(str3)
                        str4="{"+L[h]+"}"+"{"+L[l]+"}"
                        C.append(str4)
                        
    return C















def join(s1,s2):
    c=""
    s1_l=re.findall(r'\d+',s1)
    s2_l=re.findall(r'\d+',s2)
    del s1_l[0]
    last_item=s2_l[len(s2_l)-1]
    del s2_l[len(s2_l)-1]
    if s1_l==s2_l:
        
        if "," in s2[s2.rfind('{',0,len(s2))+1:s2.rfind('}',0,len(s2))]:
            c=s1[0:len(s1)-1]+","+last_item+"}"
        else:
            c=s1+"{"+last_item+"}"
            
    return c

        
        
    
    
    
    
    
def f1GenSet(LSeed,MIS):
    f1=[]
    #print "List of F1 itemsets:"
    for item in LSeed:
        if (float(countItems.get(str(item)))/float(N) >= MIS.get(item) ):
            #print item,N,float(countItems.get(str(item)))/float(N) ,MIS.get(item)
            #print item ,":",countItems.get(str(item))
            f1.append(item)
            
    #print "F1:",f1 
    return f1   

def sort(MIS,M):
       
    for i in sorted(MIS, key=MIS.get, reverse=False) :
        M.append(i)
  
     
     
    return M
    


# Rev -1  included a function confirmOrder    
#to check if a candidate sequence'c'  is present in data sequence 's'
def contains(c,s):
    temp=c
    s=s.replace(" ","")
    counter=0
    cseq=[]
    sorted_cseq=[]
    dseq=[]
    flag=[]
    
    seq_track={}
    
    #Splitting the candidate sequence into separate elements
    while temp!="":
        #cseq[counter]=temp[temp.find("{")+1:temp.find("}")].split(",")
        cseq.append(temp[temp.find("{")+1:temp.find("}")].split(","))
        temp=temp.replace("{"+temp[temp.find("{")+1:temp.find("}")]+"}","",1)
        counter=counter+1
    
        
    temp=s
    
  
    #Splitting the data sequence into separate elements
    while temp!="":
        
        #dseq[counter]=temp[temp.find("{")+1:temp.find("}")].split(",")
        
        dseq.append(temp[temp.find("{")+1:temp.find("}")].split(","))
        temp=temp.replace("{"+temp[temp.find("{")+1:temp.find("}")]+"}","",1)
        
        
    
    
    for i in range(0,len(dseq)):
        flag.append(0)
        
    
    for i in sorted(cseq,key=lambda i:len(i),reverse=True):
        sorted_cseq.append(i)
    
    #print sorted_cseq
        
        
    
    pattern=-1
    
    for can in cseq:
        
        can_str=",".join(can)
        
       
        for i in range(pattern+1,len(dseq)):
            
            #print "can:",set(can)
            #print "dat:",set(dseq[i])
            if (set(can).issubset(set(dseq[i]))) and (flag[i]==0):
                #flag[",".join(dseq[i])]=1
                pattern=i
                flag[i]=1
                break
    
  
    
    if sum(flag)==counter and confirmOrder(c,s):
        
        return 1
    else:
        return 0
                
                
            


#Checks and confirms order of items within an itemset
def confirmOrder(c,s):
    
    cand=re.findall(r'\d+',c)
    trans=re.findall(r'\d+',s)
    for i in range(1,len(cand)):
        if(trans.index(cand[i])<trans.index(cand[i-1])):
            if((len(trans)-trans[::-1].index(cand[i])-1)<(len(trans)-trans[::-1].index(cand[i-1])-1)):
                return 0
    return 1
    
# Generata a list of Item used for Fk candidate Generation
def listItem(seq) :
    ItemList = re.sub(r'\D'," ",seq).strip() 
    return ItemList.split()  
    
# Length of a sequence    
def lengthSeq(S):
    ItemList = re.sub(r'\D'," ",S).strip() 
    ListItems = ItemList.split()
#     print "Lenght :", len(ListItems)
    return len(ListItems)

# Size of a sequence
def sizeSeq(S):
    count = S.count('{')
    if(count !=S.count('}')):
        print "{ } does not match in the given sequence: ",S
        return 0
#     print "Size : ", count
    return count


# rev-1 changes '<' to '<='
# Check if first item is lesser than all in a itemset    
def checkFirstItemLesser(S,MIS):
    firstItem = S[0]
#     print firstItem
    MISFirstItem = float(MIS.get(firstItem))
    
    # check for item which has MIS value lesser than MIS First item,
    # If yes, return 0, else return 1
    for items in S[1:]:
        if(float(MIS.get(items))<=MISFirstItem ):
#             print "First Item is not lesser in S1"
            return 0
    
#     print "First Item is lesser in S1"
    return 1


# rev-1 changes '<' to '<='    
# Check if last item is lesser than all in a itemset  
def checkLastItemLesser(S,MIS):
    lastItem = S[-1]
    MISLastItem = float(MIS.get(lastItem))    
    # check for item which has MIS value lesser than MIS Last item,
    # If yes, return 0, else return 1
    for items in S[:-1]:
        if(float(MIS.get(items))<=MISLastItem):
#             print "Last Item is not lesser in S2"
            return 0
    
#     print "Last Item is lesser in S2"
    return 1
               
    
    
    
    
# returns the position of the sublist(of alist) containing the specified item       
def get_positions(xs, item):
    if isinstance(xs, list):
        for i, it in enumerate(xs):
            for pos in get_positions(it, item):
                yield (i,) + pos
    elif xs == item:
        yield ()
        
        
def prune(c,FK_1,MIS,k):
     
    #FK_1={}  
    L=[]
    sorted_MIS={}
    minitems=[]
    #print "Candudate",c
    #MIS={'12':0.014,'48':0.345,'24':0.024,'75':0.567,'123':0.989}
    
    #c="{12,24}{48,75}{123}"
    cseq=[]
    #cseq=[['12','24'],['48','75'],['123']]
    temp=c
    while temp!="":
        #cseq[counter]=temp[temp.find("{")+1:temp.find("}")].split(",")
        cseq.append(temp[temp.find("{")+1:temp.find("}")].split(","))
        temp=temp.replace("{"+temp[temp.find("{")+1:temp.find("}")]+"}","",1)
    
    #print cseq
    I=re.findall(r'\d+',c)
    N=[]
    #F[1]="{30}{40}{20}"
    #F[2]=['{30}{40}','{40}{30}']
    #F[3]=['{1}{3,5}','{4,3}{5}']
    #F[4]=["{12,24}{48,75}","{12,24}{48}{123}"]
    #print "F:",F

    #print str(10)

    for i in range(0,len(I)):
        N.append(int(I[i]))

    #Finds a list of Minitems    
    min_value=min([(MIS[x],x) for x in MIS])[0]
    for key in MIS.iterkeys():
        if MIS[key]==min_value:
            minitems.append(int(key))
    
            
    #print "minitems:",minitems
    
    
    
    prev_pat=-1
        
    
    L=list(itertools.combinations(N, k-1))
    #print L   
    sub=""
    for i in range(0,len(L)):
        
        
        sub=""
        prev_pat=-1
        for j in range(0,len(L[i])):
        
            pat=list(get_positions(cseq,str(L[i][j])))
            
            #print "Pat",pat[0][0],"Prev_pat",prev_pat
            if(pat[0][0]!=prev_pat):
                
                sub=sub+"{"+str(L[i][j])+"}"
                #print s
                
            else:
                sub=sub[:-1]+","+str(L[i][j])+"}"
                #print s
                
            
            prev_pat=pat[0][0]
        
        #print "Out",s
                
        #print "sub",sub
        #print "FK_1",FK_1
        if sub in FK_1:
            #print "Yes",sub
            return 1
        else:
            if checkmintem(sub,minitems)==1:
                #print "No",sub
                #summa=0
                return 0
                
            else:
                #print "Yes",sub
                #summa=0#
                return 1
        
        
        
        
def checkmintem(s,minitems):
    items=re.findall(r'\d+',s)
    
    for i in range(0,len(items)):
        if int(items[i]) in minitems:
            return 1
    
    return 0
        
    
     
        
    
    
      
    
if  __name__ =='__main__':main()