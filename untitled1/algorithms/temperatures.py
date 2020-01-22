import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
# min value
min = 100;
if n == 0:
    print(0)
else:
    flag = False
    one = 0
    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        one = t
        if abs(min) >= abs(t):
            if abs(min) == abs(t):
                min = abs(t)
                flag = True
            else:
                min = t
                flag = True


    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    if flag:
        print(f'{min}')
    else:
        print(one)