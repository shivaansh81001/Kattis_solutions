'''
  BEGIN-HEADER
  
  Name: SHIVAANSH BHATIA
  
  Student-ID: 1722599

  List any resources you used below (eg. urls, name of the algorithm from our code archive).
  Remember, you are permitted to get help with general concepts about algorithms
  and problem solving, but you are not permitted to hunt down solutions to
  these particular problems!

  -https://www.splashlearn.com/math-vocabulary/clock-angle-formula

  List any classmate you discussed the problem with. Remember, you can only
  have high-level verbal discussions. No code should be shared, developed,
  or even looked at in these chats. No formulas or pseudocode should be
  written or shared in these chats.

  -NONE

  By submitting this code, you are agreeing that you have solved in accordance
  with the collaboration policy in CMPUT 303/403.

  END-HEADER
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