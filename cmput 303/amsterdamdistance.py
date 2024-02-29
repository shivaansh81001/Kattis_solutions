
def calc(m,n,r,x1,y1,x2,y2):
    pi=3.14159265358979
    ans=0
    if y1<y2:
        if abs(x1-x2)*(pi/m)/2<=1.0:
            ans+=(abs(x1-x2)*(pi/m)*y1*r)/n
        else:
            ans+=(2*y1*r)/n
        ans+=(abs(y1-y2)*r)/n
    
    elif y1>y2:
        ans+=(abs(y1-y2)*r)/n
        #print(ans)
        if abs(x1-x2)*(pi/m)/2<=1.0:
            ans+=(abs(x1-x2)*(pi/m)*y2*r)/n
        else:
            ans+=(2*y2*r)/n
        #print(ans)
    
    else:
        
        if abs(x1-x2)*(pi/m)/2<=1.0:
            ans+=(abs(x1-x2)*(pi/m)*y1*r)/n
        else:
            ans+=(2*y2*r)/n
        #print(ans)
    return ans
    
    
def main():
    m,n,r=map(float,input().split())
    m,n=int(m),int(n)
    x1,y1,x2,y2=map(int,input().split())
    ans=calc(m,n,r,x1,y1,x2,y2)
    print(str(round(ans,14)))    
    

main()