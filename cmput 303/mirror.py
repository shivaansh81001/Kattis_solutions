

def main():
    test_case=int(input())
    
    
    rows=0
    cols=0
    temp=[]
    for i in range(test_case):
        
        rows_cols=input().split()
        rows=int(rows_cols[0])
        cols=int(rows_cols[1])
        temp.append([])
        for j in range(rows):
            row_inp=input()
            temp[i].append(row_inp)
          
        
    for i in range(test_case):
        print('Test',i+1)
        for j in range(len(temp[i])-1,-1,-1):
            print(temp[i][j][::-1])

        
main()           