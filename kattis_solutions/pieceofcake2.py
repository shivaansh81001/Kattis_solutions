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

inp=input().split()
side = int(inp[0])
hr_dist=int(inp[1])
vr_dist=int(inp[2])


biggest_length = 0
biggest_width = 0
if hr_dist < side/2:
    biggest_length=side-hr_dist
elif hr_dist>side/2:
    biggest_length = hr_dist
elif hr_dist == side/2:
    biggest_length = side/2

if vr_dist < side/2: 
    biggest_width = side-vr_dist
elif vr_dist > side/2:
    biggest_width = vr_dist
elif vr_dist == side/2:
    biggest_width = side/2

# print('biggest_length',biggest_length)
# print('biggest_width',biggest_width)
volume=int(biggest_length * biggest_width * 4)

print(volume)
