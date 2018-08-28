import math

def lets_add(a, b):
    sub_a = a*2
    sub_b = b*2

    mid=math.sqrt(sub_a)*math.sqrt(sub_b)
    return mid


print('5 + 2 =' + str(lets_add(5,2)))

