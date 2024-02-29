
def right(temp_board,i,j):
    if j<7:    
        if temp_board[i][j+1]=='o' and temp_board[i][j+2]=='.':
            temp_board[i][j]='.'
            temp_board[i][j+1]='.'
            temp_board[i][j+2]='o'
            return True
    return False
        
def left(temp_board,i,j):
    if j>1:    
        if temp_board[i][j-1]=='o' and temp_board[i][j-2]=='.':
            temp_board[i][j]='.'
            temp_board[i][j-1]='.'
            temp_board[i][j-2]='o'
            return True
    return  False

def up(temp_board,i,j):
    if i>1:
        if temp_board[i-1][j]=='o' and temp_board[i-2][j]=='.':
            temp_board[i][j]='.'
            temp_board[i-1][j]='.'
            temp_board[i-2][j]='o'
            return True
    return False
        
def down(temp_board,i,j):
    if i<3:
        if temp_board[i+1][j]=='o' and temp_board[i+2][j]=='.':
            temp_board[i][j]='.'
            temp_board[i+1][j]='.'
            temp_board[i+2][j]='o'
            return True
    return False
    
    
directions=[up,down,left,right]    
INF=float('inf')    
rows=5
cols=9

def print_board(board):
    for i in range (5):
        for j in range(9):
            print(board[i][j],end='')
        print('')
    print('')
    return


def count_pegs(board):
    peg=0
    for i in board:
        peg+=i.count('o')
    return peg

def hault(board):
    for i in range(5):
        for j in range(9):
            if board[i][j]=='o':
                if (i>1 and board[i-1][j]=='o' and board[i-2][j]=='.') or (i<3 and board[i+1][j]=='o' and board[i+2][j]=='.') or (j>1 and board[i][j-1]=='o' and board[i][j-2]=='.') or (j<7 and board[i][j+1]=='o' and board[i][j+2]=='.'):
                    return True
    return False
    
def game(board):
    #print_board(board)
    pegs=count_pegs(board)
    count=INF
    #prinr(pegs,count)
    if not hault(board):
        return pegs,0
    #print_board(board)
    total_pegs=pegs
    for i in range(rows):
        for j in range(cols):
            if board[i][j]=='o':
                for move in directions:
                    temp_board=list(row[:] for row in board)
                    #print(temp_board)
                    if move(temp_board,i,j):
                        new_peg,new_count=game(temp_board)
                        new_count+=1
                        if new_peg<total_pegs or (new_peg==total_pegs and new_count<count):
                            count=new_count
                            total_pegs=new_peg
    #print('----------------------------------------------------')
    return total_pegs,count


    
def main():

    cases=int(input())
    for i in range(cases):
        board=[]
        for i in range(rows):
            
            inp=list(input())
            #print(inp)
            board.append(inp)
        try:
            input()
        except:pass
        if board!=[]:
            ans=game(board)
        print(ans[0],ans[1])
        #count_pegs(board,rows,cols)
       
        #print('----------------------------------------------------')
''' 
def test():
    board=["###...###",".........","....o....",".........","###...###"]
    print(board)
    up(board)
    print(board)
    down(board)
    print(board)
    left(board)
    print(board)
    right(board)
    print(board)'''
#test()   
main()