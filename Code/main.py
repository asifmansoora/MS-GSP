'''
Created on Sep 16, 2013

@author: asifmansoor
'''
from __future__ import division
from LSeed import countItems,N
import sys,re
import itertools

    
def main():
    
    MIS={}
    count={}
    M=[]
    F={}
    L=[]
    k=1
     # L-seed list
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
    

    
    f=f1GenSet(L,MIS)
    F[k]=""
    for item in f:
        F[k]=F[k]+"{"+str(item)+"}"
    k=k+1

        
    
    
    
    
    
    
    #Converting L list  into String:
    for i in range(0,len(L)):
        L[i]=str(L[i])
        
    
     
    #Converting MIS dictionary into String: 
    for key,value in MIS.iteritems():
        del MIS[key]
        MIS[str(key)]=value
    
 
 
 
        
 #--------------------------  Inside For loop--------------------------------------------   
    # 'C' is Candidate List 
    C=level2candgen(L,MIS,countItems,sdc)
    
    print C
    
    FILE_LOC="data.txt"
    for line in open(FILE_LOC,"r"):
        s=line[line.find("<")+1:line.find(">")]
        for c in C:
            
            #check=contains("{20,30}{80,90}","{10,20,30,70}{20,30,80}{45,90}{60,70,80}")
            cnt=0
            check=contains(c,s)
            #print "check",check
            if(check==1):
                if c not in count:
                    count[c]=1
                else:
                    count[c]=count[c]+1
            
 
 
 
 
                    
    
 
 
 
    
    print count
    F[k]=gen_F(C,MIS,count)
    
    print F
    
    
    print "Join"
    c=join("{1}{2}{3}","{1}{2}{3}")
    
    print "test"
    
   
#---------------------------- For loop ends here ----------------------------------------


#candidate Generation for F[k]
def CandGen(fkth,MIS):
    
    fkth = ['<{1},{4},{5}>','<{1},{4},{6}>','<{1},{5},{6}>','<{1},{5,6}>','<{1},{6},{3}>','<{6},{3},{6}>','<{5,6},{3}>','<{5},{4},{3}>','<{4},{5},{3}>']
    fKsplit =[]
    candList =[]

    for seq in fkth:
        fKsplit.append((seq.replace("<","")).replace(">",""))
        print fKsplit


    for s1Seq in fKsplit:
        s1 = s1Seq
        print "s1: ",s1

        for s2Seq in fKsplit:
            # s1 and s2 can be equal
            #if s1 == s2Seq:
                #print "s1=s2 :",s2Seq
                #continue

            
            s2 = s2Seq
            #print "s2 is different, s2 :",s2 
            
            listS1 = listItem(s1)
            listS2 = listItem(s2)
            
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
    
                print "s1 :",(','.join(listS1))
                print "s2 :",(','.join(listS2))
                    
                print "MIS last s2: ",MISlastS2
                print "MIS first s1: ",MISfirstS1
                print("LastItemS1 :", int(lastItemS1))
                print("LastItemS2 :", int(lastItemS2))
                if((','.join(listS1) == ','.join(listS2)) and (MISlastS2 > MISfirstS1)):
                    # append last item with '{' '}' to check for matching substring
                    lastElemS2 = "{"+lastItemS2 +"}"
                    print "lastElemS2",lastElemS2 
                    
                    #check if the last item is an element in s2
                    if(s2.rfind(lastElemS2)==(len(s2)-len(lastElemS2))):
                        withLastElemS1=s1+","+lastElemS2
                        print "c1 candidate :",withLastElemS1
                        candList.append(withLastElemS1)
                        if((lengthSeq(s1) == 2) and (sizeSeq(s1)==2) and (int(lastItemS2)>int(lastItemS1))):
                            lastElemItemS1 = s1[:len(s1)-1] +','+lastItemS2+s1[len(s1)-1:]
                            print "c2 candidate :", lastElemItemS1
                            candList.append(lastElemItemS1)
                    
                    # else if the last item is not a separate element
                    
                    elif( ( (lengthSeq(s1)==2 and sizeSeq(s1)==1) and (int(lastItemS2)>int(lastItemS1))) or (lengthSeq(s1) >2)) :
                        ItemtoLastElemS1 = s1[:len(s1)-1] +','+lastItemS2+s1[len(s1)-1:]
                        print "Item added to last element of S1: ", ItemtoLastElemS1
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
    
                print "s1 :",(','.join(listS1))
                print "s2 :",(','.join(listS2))
                    
                print "MIS last s2: ",MISlastS2
                print "MIS first s1: ",MISfirstS1
                print("LastItemS1 :", int(lastItemS1))
                print("LastItemS2 :", int(lastItemS2))
                if((','.join(listS1) == ','.join(listS2)) and (MISlastS2 < MISfirstS1)):
                    # append first item with '{' '}' in S1 to check for matching substring
                    firstElemS1 = "{"+firstItemS1 +"}"
                    print "firstElemS1: ",firstElemS1 
                    #check if the First item is an first element in s1
                    if(s1.find(firstElemS1)==0):
                        withFirstElemS2=firstElemS1+","+s2
                        print "c1 candidate :",withFirstElemS2
                        candList.append(withFirstElemS2)
                        if((lengthSeq(s2) == 2) and (sizeSeq(s2)==2) and (int(firstItemS1)<int(firstItemS2))):
                            firstElemItemS2 = s2[:1]+firstItemS1+','+s2[1:]
                            print "c2 candidate :", firstElemItemS2
                            candList.append(firstElemItemS2)
                    
                    # if first item is not a separate element in s1
                    elif( ( (lengthSeq(s2)==2 and sizeSeq(s2)==1) and (int(firstItemS2)>int(firstItemS1))) or (lengthSeq(s2) >2)) :
                        ItemtoFirstElemS2 = s2[:1]+firstItemS1+','+s2[1:]
                        print "Item added to first element of S2: ", ItemtoFirstElemS2 
                        candList.append( ItemtoFirstElemS2 )
            
            # Join using normal operation
            else:
                 candList.append((join(s1,s2)))           
            
    # Print candidate list before pruning
    print candList
    





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
    C=[]
    for l in range(0,len(L)):
        #print "I:",L[l],"C:",(countItems[L[l]])/float(N),"M:",MIS[L[l]]
        if float(countItems[L[l]])/float(N) >= MIS[L[l]]:
            
                                
            for h in range(l+1,len(L)):
                #print "H:",L[h],"C:",(countItems[L[h]])/float(N),"M:",MIS[L[l]]
                if (countItems[L[h]]/float(N) >= MIS[L[l]]) and abs((countItems[L[h]]/float(N))-(countItems[L[l]]/float(N)))<=1.00:
                    
                    str1="{"+L[l]+","+L[h]+"}"
                    C.append(str1)
                    str2="{"+L[l]+"}"+"{"+L[h]+"}"
                    C.append(str2)
                        
    return C

def level2candgen(L,MIS,countItems,sdc):
    C=[]
    print "L:",L
    for l in range(0,len(L)):
        #print "I:",L[l],"C:",(countItems[L[l]])/float(N),"M:",MIS[L[l]]
        if float(countItems[L[l]])/float(N) >= MIS[L[l]]:
            
                                
            for h in range(0,len(L)):
                #print "H:",L[h],"C:",(countItems[L[h]])/float(N),"M:",MIS[L[l]]
                if(h!=l):
                    if (countItems[L[h]]/float(N) >= MIS[L[l]]) and abs((countItems[L[h]]/float(N))-(countItems[L[l]]/float(N)))<=1.00:
                        str1="{"+L[l]+","+L[h]+"}"
                        C.append(str1)
                        str2="{"+L[l]+"}"+"{"+L[h]+"}"
                        C.append(str2)
                        
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
    for item in LSeed:
        if (float(countItems.get(str(item)))/float(N) >= MIS.get(item) ):
            #print item,N,float(countItems.get(str(item)))/float(N) ,MIS.get(item)
            f1.append(item)
            
    print "F1:",f1 
    return f1   

def sort(MIS,M):
       
    for i in sorted(MIS, key=MIS.get, reverse=False) :
        M.append(i)
  
     
     
    return M
    
    
#to check if a candidate sequence'c'  is present in data sequence 's'
def contains(c,s):
    temp=c
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
    
  
    
    if sum(flag)==counter:
        return 1
    else:
        return 0
                
                
            
                #pattern=pattern+(i+1)
                #seq_track[can_str]=pattern
    
   
  #  if (len(set(seq_track.values()))==1 or len(set(seq_track.values()))==counter) and (len(set(seq_track.keys()))==counter):
   #     print "Sum:",seq_track.values(),len(set(seq_track.values()))
    #    return 1
  #  else:
   #     return 0
        

# Generata a list of Item used for Fk candidate Generation
def listItem(seq) :
    ItemList = re.sub(r'\D'," ",seq).strip() 
    return ItemList.split()  
    
# Length of a sequence    
def lengthSeq(S):
    ItemList = re.sub(r'\D'," ",S).strip() 
    ListItems = ItemList.split()
    print "Lenght :", len(ListItems)
    return len(ListItems)

# Size of a sequence
def sizeSeq(S):
    count = S.count('{')
    if(count !=S.count('}')):
        print "{ } does not match in the given sequence: ",S
        return 0
    print "Size : ", count
    return count

# Check if first item is lesser than all in a itemset    
def checkFirstItemLesser(S,MIS):
    firstItem = S[0]
    MISFirstItem = float(MIS.get(firstItem))
    
    # check for item which has MIS value lesser than MIS First item,
    # If yes, return 0, else return 1
    for items in S[1:]:
        if(float(MIS.get(items))<MISFirstItem ):
            print "First Item is not lesser in S1"
            return 0
    
    print "First Item is lesser in S1"
    return 1
    
# Check if last item is lesser than all in a itemset  
def checkLastItemLesser(S,MIS):
    lastItem = S[-1]
    MISLastItem = float(MIS.get(lastItem))    
    # check for item which has MIS value lesser than MIS Last item,
    # If yes, return 0, else return 1
    for items in S[:-1]:
        if(float(MIS.get(items))<MISLastItem):
            print "Last Item is not lesser in S2"
            return 0
    
    print "Last Item is lesser in S2"
    return 1
               
    
    
    
    
# returns the position of the sublist(of alist) containing the specified item       
def get_positions(xs, item):
    if isinstance(xs, list):
        for i, it in enumerate(xs):
            for pos in get_positions(it, item):
                yield (i,) + pos
    elif xs == item:
        yield ()
        
        
def prune(c,s,F,MIS):
     
    subseqs=[]
    #c="{12,24}{48,75}{123}"
    cseq=[]
    #cseq=[['12','24'],['48','75'],['123']]
    temp=c
    while temp!="":
        #cseq[counter]=temp[temp.find("{")+1:temp.find("}")].split(",")
        cseq.append(temp[temp.find("{")+1:temp.find("}")].split(","))
        temp=temp.replace("{"+temp[temp.find("{")+1:temp.find("}")]+"}","",1)
    
    #print cseq
    
    #Extracts all numbers from the string
    data=re.findall(r'\d+',c)
    N=[]
    
    #Converts numbers from string format into int format
    for i in range(0,len(data)):
        N.append(int(data[i]))

    
    prev_pat=-1
        
    #Produces subsequences  if length k-1
    subseqs=list(itertools.combinations(N, k-1))
    print subseqs   
    s=""
    
    #Inserts brackets at correct positions for the subsequence
    for i in range(0,len(subseqs)):
        
        
        s=""
        prev_pat=-1
        for j in range(0,len(subseqs[i])):
        
            pat=list(get_positions(cseq,str(subseqs[i][j])))
            
            #print "Pat",pat[0][0],"Prev_pat",prev_pat
            if(pat[0][0]!=prev_pat):
                
                s=s+"{"+str(subseqs[i][j])+"}"
                #print s
                
            else:
                s=s[:-1]+","+str(subseqs[i][j])+"}"
                #print s
                
            
            prev_pat=pat[0][0]
        
        print "Out",s
        
        if s in F:
            print "yes"

    
     
        
    
    
      
    
if  __name__ =='__main__':main()