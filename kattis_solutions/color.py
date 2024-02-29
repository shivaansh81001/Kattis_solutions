'''
  BEGIN-HEADER
  
  Name: SHIVAANSH BHATIA
  
  Student-ID: 1722599

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  -https://stackoverflow.com/questions/5549141/how-to-finish-sys-stdin-readlines-input
  
  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  -NONE

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
'''
import sys
def machines(num_of_socks,max_cap,diff,socks):
    machine=0
    cap=0
    temp=None
    #print(socks)
    for i in socks:
        #print(temp,i)
        if temp==None or abs(i-temp)<=diff:
            cap+=1
            #print(temp)
            if cap>=max_cap:
                #print('hi')
                temp=None
                machine+=1
                cap=0
            else:
                temp=i
        else:
            machine+=1
            cap=1
            temp=i
    #print(machine)
    if cap!=0:
        machine+=1

    return machine

def main():
    inp=list(map(int,sys.stdin.readline().split()))
    #lines = [item.rstrip('\r\n') for item in lines]
    socks=sorted(list(map(int,sys.stdin.readline().split())))
    #inp=[eval(i) for i in input().split()]
    #socks=[eval(i) for i in input().split()]
    
    num_of_socks=inp[0]
    max_cap=inp[1]
    diff=inp[2]
    #print('diff',diff)
    #socks=sorted(socks)
    #print(socks)
    ans=machines(num_of_socks,max_cap,diff,socks)
    print(ans)
main()