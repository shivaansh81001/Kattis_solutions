'''
  BEGIN-HEADER
  
  Name: SHIVAANSH BHATIA
  
  Student-ID: 1722599

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  -https://www.geeksforgeeks.org/longest-common-substring-array-strings/

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  -NONE

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
'''
def check(sub,strs):
    for i in strs:
        if sub not in i:
            return False
    return True
    
def lcs(strs):
    strs=sorted(strs,key=lambda x:len(x))
    temp=strs[0]
    #print(temp,len(temp))
    for i in range(len(temp),0,-1):
        for j in range(len(temp)-i+1):
            sub=temp[j:j+i]
            #print(sub)
            if check(sub,strs):
                return sub
    return ''
    
def main():
    cases=int(input())
    strs=[]
    
    for i in range(cases):
        strs.append(input())
    strs=sorted(strs,key=lambda x: len(x))
    #print(strs)
    if len(strs)==1:
        print(len(strs[0]))
    
    else:
        ans=lcs(strs)
        print(len(ans))
main()