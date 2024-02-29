'''

  -https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/FenwickTree.py

'''

class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def findkth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1
        
    def repr(self):
        return self.bit
        

    
def main():
    n,q=map(int,input().split())
    vals=list(map(int,input().split()))
    gems=input()
    #print(gems)
    data=[]
    for i in gems:
        data.append(int(i)-1)
    data=[0]+data
    #print(data)
    
    trees=[]
    for i in range(6):
        trees.append(FenwickTree([0]*(n+1)))
    #print(trees)   
    for i in range(1,n+1):
        trees[data[i]].update(i,1)
        
    for i in range(q):
        task,arg1,arg2=map(int, input().split())
        if task==1:
            trees[data[arg1]].update(arg1,-1)
            data[arg1]=arg2-1
            trees[data[arg1]].update(arg1,1)
            
        elif task==2:
            vals[arg1-1]=arg2
            #print(trees[data[arg1]].repr())
            
        else:
            ans=0
            for i in range(6):
                temp=(trees[i].query(arg2+1)-trees[i].query(arg1))*vals[i]
                ans+=temp
            print(ans)

main()