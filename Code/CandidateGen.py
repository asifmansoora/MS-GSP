'''
Created on Sep 22, 2013

@author: asifmansoor
'''
import re

     
def listItem(seq) :
    ItemList = re.sub(r'\D'," ",seq).strip() 
    return ItemList.split()  
    
    
def lengthSeq(S):
    ItemList = re.sub(r'\D'," ",S).strip() 
    ListItems = ItemList.split()
    print "Lenght :", len(ListItems)
    return len(ListItems)

def sizeSeq(S):
    count = S.count('{')
    if(count !=S.count('}')):
        print "{ } does not match in the given sequence: ",S
        return 0
    print "Size : ", count
    return count
    
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
            if s1 == s2Seq:
                print "s1=s2 :",s2Seq
                continue

            
            s2 = s2Seq
            print "s2 is different, s2 :",s2 
            
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
                        
            
    print candList
   