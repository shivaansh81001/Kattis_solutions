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
import math


def dist(a,b,c,x_p,y_p):
    return abs((a*x_p)+(b*y_p)+c)/(math.sqrt((a*a)+(b*b)))

def line(x1,y1,x2,y2,x_p,y_p):
    a=y2-y1
    b=x1-x2
    c=x2*y1-x1*y2
    #print(a,b,c)
    return dist(a,b,c,x_p,y_p)

def least(city):
    #print(city)
    temp=-1
    for i in city.keys():
        #print(temp)
        if temp!=-1:
            if city[i]<temp:
                temp=city[i]
        else:
            temp=city[i]
    
    for j in city.keys():
        if city[j]==temp:
            print(j,end=' ')
    print('')
'''   
def test():
    #ret=line(3,3,12,12)
    #print(ret)
    print(line(1,1,2,1,5,2))
    print(dist(1,1,2,1,5,2))
'''  
    
def main():
    cases=int(input())
    for i in range(cases):
        x1,y1,x2,y2=map(int,input().split())
        city={}
        cities=int(input())
        
        for j in range(cities):
            inp=input().split()
            x_p=int(inp[1])
            y_p=int(inp[2])
            
            ret=line(x1,y1,x2,y2,x_p,y_p)
            city[inp[0]]=ret
        least(city)
        
main()