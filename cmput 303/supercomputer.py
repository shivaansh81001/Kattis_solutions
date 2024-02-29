'''
 
  -https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/SegmentTree.py

'''
class SegmentTree:
    def __init__(self, data, default=0, func= lambda x,y:x+y):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (4* _size)
        
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

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

def main():
    n,k=map(int, input().split())
    data=[0]*n
    tree=SegmentTree(data)
    #print(tree.__repr__())
    for i in range(k):
        inp=input().split()
        if inp[0]=='F':
            pos=int(inp[1])
            temp=tree.__getitem__(pos-1)
            tree.__setitem__(pos-1,1-temp)
            #print(tree.__repr__())
        elif inp[0]=='C':
            start=int(inp[1])-1
            end=int(inp[2])-1
            #print(start,end)
            print(tree.query(start,end+1))
            #print(tree.__repr__())

main()