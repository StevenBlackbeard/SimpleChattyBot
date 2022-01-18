angle_1 = int(input())
angle_2 = int(input())
angle_3 = int(input())
angle_sum = 180

if sum((angle_1, angle_2, angle_3)) == angle_sum:
    print("The triangle is valid!")
else:
    print("The triangle is not valid!")