'''
  BEGIN-HEADER
  
  Name: SHIVAANSH BHATIA
  
  Student-ID: 1722599

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  -https://github.com/cheran-senthil/PyRival/blob/master/pyrival/geometry/lines.py

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  -NONE

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
'''

import itertools 
prec=0.000001
class Points:
    def __init__(self,x,y):
        self.x_coord=x
        self.y_coord=y


def intersect(l1,l2):
    #print(l1[1][1])
    a1=l1[1][1]-l1[0][1]
    b1=l1[0][0]-l1[1][0]
    c1=a1*l1[0][0]+b1*l1[0][1]
    
    a2=l2[1][1]-l2[0][1]
    b2=l2[0][0]-l2[1][0]
    c2=a2*l2[0][0]+b2*l2[0][1]
    
    det=a1*b2-a2*b1
    if abs(det)<prec:
        return None
    else:
        x=(b2*c1-b1*c2)/det
        y=(a1*c2-a2*c1)/det
        
    return (x,y)
    
    
def colinear(p1,p2):
    return (abs(p1[1]-p2[1])>prec) or (abs(p1[0]-p2[0])>prec)
    
def check(p,p1,p2):
    return min(p1,p2)<=p<=max(p1,p2)
    
    
def possible(l1,l2):
    temp=intersect(l1,l2)
    if temp is not None:
        return check(temp[0],l1[0][0],l1[1][0]) and check(temp[0],l2[0][0],l2[1][0]) and check(temp[1],l1[0][1],l1[1][1]) and check(temp[1],l2[0][1],l2[1][1])
    else:
        return False
        
        
def is_triangle(l1,l2,l3):
    if not (possible(l1,l2) and possible(l2,l3) and possible(l3,l1)):
        return False
    p1,p2,p3=intersect(l1,l2),intersect(l2,l3),intersect(l3,l1)
    
    return colinear(p1,p2) and colinear(p2,p3) and colinear(p3,p1)

def main():
    while True:
        inp=int(input())
        if inp==0:
            break
        lines=[]
        for i in range(inp):
            x1,y1,x2,y2 = map(float, input().split())
            point_1=Points(round(x1, 6), round(y1, 6))
            point_2=Points(round(x2, 6), round(y2, 6))
            p1=(point_1.x_coord, point_1.y_coord)
            p2=(point_2.x_coord, point_2.y_coord)
            #print(p1,p2)
            lines.append((p1,p2))
            #print(lines)
        ans=0
        for l1,l2,l3 in itertools.combinations(lines,3):
            #print(l1,l2,l3)
            #print('l1.y2',l1[1][1])
            if is_triangle(l1,l2,l3):
                ans+=1
        print(ans)
main()