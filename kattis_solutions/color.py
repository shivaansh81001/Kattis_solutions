'''


  -https://stackoverflow.com/questions/5549141/how-to-finish-sys-stdin-readlines-input

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