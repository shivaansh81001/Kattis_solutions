'''
  BEGIN-HEADER
  
  Name: SHIVAANSH BHATIA
  
  Student-ID: 1722599

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  -NONE

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
    test_case=int(input())
    
    
    rows=0
    cols=0
    temp=[]
    for i in range(test_case):
        
        rows_cols=input().split()
        rows=int(rows_cols[0])
        cols=int(rows_cols[1])
        temp.append([])
        for j in range(rows):
            row_inp=input()
            temp[i].append(row_inp)
          
        
    for i in range(test_case):
        print('Test',i+1)
        for j in range(len(temp[i])-1,-1,-1):
            print(temp[i][j][::-1])

        
main()           