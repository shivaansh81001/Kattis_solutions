'''
  -https://www.geeksforgeeks.org/longest-common-substring-array-strings/

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