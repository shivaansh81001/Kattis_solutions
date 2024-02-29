
def remaining_teams(N,S,R,inp2,inp3):
    for i in range(len(inp2)):
        #print('i',inp2[i])
        for j in range(len(inp3)):
            #print('j',inp3[j])
            if inp2[i]=='*' or inp3[j]=='*':
                    pass
            else:
                if abs(inp2[i]-inp3[j])<=1:
                    
                    inp2[i]='*'
                    inp3[j]='*'
             
    #print(inp2,inp3)   
    temp =0
    for i in inp2:
        if i!='*':
            temp+=1
    return temp


def main():
    inp1=input().split()
    inp1=[eval(i) for i in inp1]
    
    inp2=input().split()
    inp2=[eval(i) for i in inp2]
    
    inp3=input().split()
    inp3=[eval(i) for i in inp3]
    
    N=inp1[0]
    S=inp1[1]
    R=inp1[2]
    
        
    ans=remaining_teams(N,S,R,inp2,inp3)
    print(ans)
    
main()