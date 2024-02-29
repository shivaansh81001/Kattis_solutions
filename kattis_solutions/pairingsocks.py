
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

def pair(socks_list):
    arb=[]
    step=0
    while len(socks_list)!=0:
        
        # if len(arb)==len(set(arb)):
        #     print('impossible')
        #     return

        if len(arb)!=0 and arb[-1]==socks_list[-1]:
            socks_list.pop()
            arb.pop()
            
            step+=1
        else:
            
            popped=socks_list.pop()
            arb.append(popped)
            step+=1
        # print('socks=',socks_list,'arb=',arb)
    if len(arb)==0:
        
        return step
    else:
        
        return 'impossible'
def main():
    pairs= int(input())
    
    socks_list=list(map(int,input().split()))
    ans=pair(socks_list)
    print(ans)
    # 
    
         
    # if len(socks_list)!=0:
    #     popped= socks_list.pop(0)
    #     arb.insert(0, popped)
    #     step+=1
        

main()