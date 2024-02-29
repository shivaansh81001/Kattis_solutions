'''
  -https://www.splashlearn.com/math-vocabulary/clock-angle-formula

'''

def calc(angle):
    overlaps=[]
    first_half=[]
    second_half=[]
    for i in range(0,26,5):
        first_half.append(i)
        second_half.append(i+30)
    #print(first_half,second_half)
    for i in range(6):
        overlaps.append(first_half[i])
        overlaps.append(second_half[i])
    #print(overlaps)
    angle+=(3600*(overlaps.index(angle%55)))
    minutes=int(angle/55)

    hours,mins=int(minutes/60),minutes%60
    print(f"{hours:02d}:{mins:02d}")
    
def main():
    inp=int(input())
    calc(inp)
    
main()