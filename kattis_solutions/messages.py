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
def calc(string,words):
    ans=0
    temp=[]
    for i in words:
        try:
            pos = string.find(i)
        except:
            continue
        while pos!=-1:
            temp.append((pos,pos+len(i)-1))
            pos=pos+1
            pos=string.find(i,pos)
    #print(temp)
    temp=sorted(temp,key=lambda x:x[1])
    #print(temp)
    end=-1
    for i in temp:
        if i[0]<=end:
            pass
        else:
            end=i[1]
            ans+=1
    return ans
    
    
def main():
    words=[]
    while True:
        inp=input()
        if inp=='#':
            break
        words.append(inp)
    #print(words)
    
    temp=""
    while True:
        inp=input()
        if inp == "#":
            break
        temp+=inp
        #print(temp)
        if temp.endswith('|'):
            #print(temp[:-1])
            ans=calc(temp[:-1],words) 
            print(ans)
            temp=""

main()