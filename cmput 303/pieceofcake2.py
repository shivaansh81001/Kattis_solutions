

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
