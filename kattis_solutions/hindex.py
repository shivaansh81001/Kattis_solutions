'''
  
  -https://subjectguides.uwaterloo.ca/calculate-academic-footprint/YourHIndex

'''

def main():
    
    papers =int(input())
    
    temp=[]
    for i in range(papers):
        temp.append(int(input()))
     
    temp.sort()
    temp.reverse()
    
    hindex=0
    for i in range(papers):
        if temp[i]<i+1:
            break
        else:
            hindex+=1
        
    print(hindex)
    
if __name__=='__main__':
    main()