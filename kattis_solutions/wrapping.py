'''

  -https://github.com/cheran-senthil/PyRival/tree/master/pyrival/geometry
  -https://stackoverflow.com/questions/34372480/rotate-point-about-another-point-in-degrees-python

'''
import math

class Point:
    def __init__(self,x,y):
        self.x_coord=x
        self.y_coord=y
        
        
def remove_middle(a, b, c):
    cross = (a[0] - b[0]) * (c[1] - b[1]) - (a[1] - b[1]) * (c[0] - b[0])
    dot = (a[0] - b[0]) * (c[0] - b[0]) + (a[1] - b[1]) * (c[1] - b[1])
    return cross < 0 or cross == 0 and dot <= 0


def convex_hull(points):
    spoints = sorted(points)
    hull = []
    for p in spoints + spoints[::-1]:
        while len(hull) >= 2 and remove_middle(hull[-2], hull[-1], p):
            hull.pop()
        hull.append(p)
    hull.pop()
    return hull


    
def hull_area(hull):
    #print(hull, hull[1:] + hull[:1])
    return abs(sum(i[0] * j[1] - j[0] * i[1] for i, j in zip(hull, hull[1:] + hull[:1])))/2
  
  
def rotate(p, angle, c):
    angle=math.radians(angle)
    x = p[0]-c[0]
    y = p[1]-c[1]
    temp= math.sqrt(x** 2 + y ** 2)
    old = math.atan2(y, x)
    angle = -angle + old
    newx = temp * math.cos(angle)
    newy = temp * math.sin(angle)
    return (c[0] + newx, c[1] + newy)
    
    
def main():
    cases=int(input())
    for i in range(cases):
        inp=int(input())
        area=0
        points=[]
        for j in range(inp):
            x,y,w,h,v=map(float,input().split())
            point=Point(x,y)
            #print(x,y,w,h,v)
            area=area+(w*h)
            p=(point.x_coord,point.y_coord)
            w,h=w/2,h/2
            #print('---',w,h)
            #print(area)
            #print('=',p[0]+w,p[1]+h)
            #print('***',p[0],p[1])
            ps=[rotate((p[0]+w,p[1]+h),v,(p[0],p[1])),rotate((p[0]+w,p[1]-h),v,(p[0],p[1])),rotate((p[0]-w,p[1]+h),v,(p[0],p[1])),rotate((p[0]-w,p[1]-h),v,(p[0],p[1]))]
            #print(ps)
            points.extend(ps)
        #for i in points:
            #print(i[0],i[1])
        
        hull=convex_hull(points)
        #print(hull)
        total=hull_area(hull)
        ans=(area/total)*100
        print(f"{ans:.1f} %")
        
            

main()