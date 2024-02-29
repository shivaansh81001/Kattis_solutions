
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