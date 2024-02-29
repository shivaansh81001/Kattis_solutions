'''
  BEGIN-HEADER
  
  Name: SHIVAANSH BHATIA
  
  Student-ID: 1722599

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  -NONE

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  -NONE

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
'''
wknds=set()
wkdys=set([0,6])

def min_pop(times):
    if not times:
        return None
    else:
        smallest_value=min(times)
        smallest_index=times.index(smallest_value)
        return times.pop(smallest_index) 
    
def solve(m,p,skip,moves):
    ans,i=0,1
    times=[]
    l=len(moves)
    while i<101:
        while ans<l and moves[ans][0] <= i:
            times.append(moves[ans][1])
            ans=ans+1
        if (i%7) in skip:
            pass
        else:
            j=0
            while j<int(p/2):
                if times:
                    pass
                else:
                    break
                min_pop(times)
                j+=1
        if not times and ans==l:
            break
        if times and min(times)<=i:
            return False
        i+=1
    return True


    

def main():
    cases=int(input())
    for i in range(cases):
        m,p=map(int, input().split())
        moves=[]
        for i in range(m):
            moves.append(tuple(map(int,input().split())))
        moves = sorted(moves)
        if solve(m,p,wkdys,moves):
            print("fine")
        elif solve(m,p,wknds,moves):
            print("weekend work")
        else:
            print("serious trouble")
            

main()