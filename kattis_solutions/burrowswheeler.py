'''


  -https://www.rahmannlab.de/lehre/alsa21/02-3-sais.pdf
  -https://www.geeksforgeeks.org/suffix-array-set-2-a-nlognlogn-algorithm/

  
'''
def key(rank,x,temp,l):
    return (rank[x], rank[(x+temp)%l])
    
def cmp(suff,rank,temp,l,sorting):
    for i in range(1, l):
        if (rank[suff[i-1]],rank[(suff[i-1]+temp)%l])==(rank[suff[i]],rank[(suff[i]+temp)%l]):
            sorting[suff[i]]=sorting[suff[i-1]]
        else:
            sorting[suff[i]]=sorting[suff[i-1]]+1
    #print(sorting)
    return sorting

def constructSA(inp):
    
    suff=list(range(len(inp)))
    l=len(inp)
    rank=inp[:]

    temp=1
    while temp<l:
        suff=sorted(suff,key=lambda x: key(rank,x,temp,l))
        sorting = [0] * l
        sorting[suff[0]] = 0
        rank = cmp(suff,rank,temp,l,sorting)
        temp=temp*2

    return suff

def main():
    while True:
        try:
            inp=input()
            if inp=='':
                break
            ans=''
            suff=constructSA(inp)
            for i in suff:
                ans+=inp[i-1]
            print(ans)
        except:break
    
        
main()