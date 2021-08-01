import bext
import random
import time
import os

def clear():
        _ = os.system('cls')

dim = bext.size()
width = dim[0]
height = dim[1]
#print(width,"  ",height)
x_init = random.randint(0,width-1)
y_init = random.randint(0,height-1)
x_speed = 1
y_speed = 1
bext.fg('random')
bext.goto(x_init,y_init) 
print('DVD')
clear()

while True:
    x = x_init + x_speed
    y = y_init + y_speed
    if x == width-1 or x == 0:
        x_init = x
        y_init = y
        x_speed = x_speed*-1
        bext.fg('random')
    elif y == height-1 or y == 0:
        x_init = x
        y_init = y
        y_speed = y_speed*-1
        bext.fg('random')
    bext.goto(x,y) 
    print('DVD')
    x_init = x
    y_init = y
    time.sleep(0.05)
    clear()
