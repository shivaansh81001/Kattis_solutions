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

def check(word,dictn):
    #print(word)
    if word in dictn:
        return True
    return False
    
def calc(sign,word,dictn,temp):
    #print(sign)
    if sign=='+':
        temp+=dictn[word]
    elif sign=='-':
        temp-=dictn[word]
    return temp
        
def result(inp, dictn):
    #print(inp)
    if inp[0] in dictn:
        temp=dictn[inp[0]]
    else:
        return 'unknown'
    for i in range(1,len(inp)-1,2):
        sign,word=inp[i],inp[i+1]
        if check(word,dictn):
            t=calc(sign,word,dictn,temp)
            temp=t
        else:
            return 'unknown'
    
    for i,j in dictn.items():
        if j==temp:
            return i
    return 'unknown'
            
            
         
def main():
    dictn={}
    while(1):
        try:
            inp=input().split()
        except:
              break  
        #print(inp)
        if inp[0]=='clear':  
            dictn.clear()
            
        elif inp[0]=='def':
            dictn[inp[1]]=int(inp[2])
            
        if inp[0]=='calc':
            res=result(inp[1:],dictn)
            #print(dictn)
            print(' '.join(map(str,inp[1:])),res)
        
    
main()