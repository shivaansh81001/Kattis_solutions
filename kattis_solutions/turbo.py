'''
  BEGIN-HEADER
  
  Name: SHIVAANSH BHATIA
  
  Student-ID: 1722599

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  -https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/SegmentTree.py

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  -NONE

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
'''
class SegmentTree:
    def __init__(self, data, default=0, func=lambda x,y:x+y):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[2*i], self.data[2*i + 1])
    
    def update(self, idx, value):
        idx += self._size
        self.data[idx] = value
        while idx > 1:
            idx >>= 1
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            
    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)

def calc(tree,n,num,index,inc=0):
    start,end=0,n-1
    #print(tree.__repr__())
    while inc<n:
        tree.update(inc,1)
        inc+=1
    #print(tree.__repr__())
    for i in range(1,n+1):
        if i%2==0:
            tree.update(index[end],0)
            print(tree.query(index[end],n))
            end-=1
            #print(end)
            #print(tree.__repr__())
        else:
            tree.update(index[start],0)
            print(tree.query(0,index[start]+1))
            start+=1
            #print(start)
            #print(tree.__repr__())
        
    
def main():
    n=int(input())
    num,index=[0]*n,[0]*n
    tree=SegmentTree(num)
    #print(tree.__repr__())
    for i in range(n):
        inp=int(input())
        num[i]=inp
        index[inp-1]=i
    #print(num,index)
    calc(tree,n,num,index)   
    
    
    
    
main()