import sys

def main():
    
    FILE_LOC="C:\\Users\\balachandar\\Desktop\\Study\\Fall_2013\\Projects\\DM\\MSGSP\\para.txt"
    MIS={}
    M=[]
    L=[13,45,27,9,56,56]
    
    
    for line in open(FILE_LOC,"r"):
        if(("SDC" or "sdc")  not in line):
            key=int(line[line.find("(")+1:line.find(")")])
            value=float(line[line.find("=")+1:].strip("\n"))
            MIS[key]=value
            
        else:
          sdc=float(line[line.find("=")+1:].strip("\n"))
          
    
       
    M=sort(MIS,M)
    print M
    
    


def level2candidategen():
    
    
    
    
    
    
    
def sort(MIS,M):
       
    for i in sorted(MIS, key=MIS.get, reverse=False) :
        M.append(i)
   
    return M
    
  
    
if  __name__ =='__main__':main()