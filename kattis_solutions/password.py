
def main():
    dictn={}
    n=int(input())
    for i in range(n):
        word,p=map(str,input().split())
        dictn[word]=float(p)
    dictn={k:v for k,v in sorted(dictn.items(),key=lambda item:item[1],reverse=True)}
    ans=0
    vals=list(dictn.values())
    for i in range(1,n+1):
        ans+=(i*vals[i-1])
    print(ans)
main()