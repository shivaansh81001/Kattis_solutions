'''
  BEGIN-HEADER
  
  Name: SHIVAANSH BHATIA
  
  Student-ID: 1722599

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  -https://subjectguides.uwaterloo.ca/calculate-academic-footprint/YourHIndex

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  -NONE

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
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