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
def calc(dictn,corr,s,cnc):
    total=1
    correct=1
    status='correct'
    for i in s:
        total*=len(dictn.get(i))
        correct*=corr[i]
    if total!=1:
        print(correct,'correct')
        print(total-correct,'incorrect')
    else:
        for i in s:
            print(dictn.get(i)[0],end=" ")
            #print(cnc[i])
            if cnc[i][0]=='correct':
                pass
            else:status='incorrect'
        print('')
        print(status)
    
    
def main():
    n=int(input())
    s=input().split()
    #print(s)
    m=int(input())
    dictn={}
    corr={}
    cnc={}
    for i in range(m):
        d,e,c=map(str,input().split())
        if d not in dictn and d not in cnc:
            dictn[d]=[e]
            corr[d]=0
            cnc[d]=[c]
        else:
            cnc[d].append(c)
            dictn[d].append(e)
        if c=='correct':
            corr[d]+=1
    #print(dictn,corr,cnc)
    calc(dictn,corr,s,cnc)
    
main()