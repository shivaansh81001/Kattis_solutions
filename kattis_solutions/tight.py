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
def solve(k,n):
    #print('hi')
    arr=[]
    for i in range(n):
        arr.append([0]*(k+3))
    #print(arr)
    
    j=0
    while j<k+1:
        arr[0][j+1]=1
        j+=1
    #print(arr)
    m=1
    while m<n:
        l=0
        while l<k+1:
            arr[m][l+1]=arr[m-1][l]+arr[m-1][l+2]+arr[m-1][l+1]
            l+=1
        m+=1
    #print(arr)
    den,num=(k+1)**n,sum(arr[n-1][1:k+2])
    #print(den,num)
    return num,den

def main():
    while True:
        try:
            k,n=map(int,input().split())
            #print(k,n)
            if k==0:
                print(100.0)
            else:
                num,den=solve(k,n)
                ans=(num/den)*100.0
                print(f"{ans:.12f}")
        except:
            break

main()