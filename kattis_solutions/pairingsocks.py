

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