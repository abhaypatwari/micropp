import bext
import random
import time
import os

def clear():
        _ = os.system('cls')

dim = bext.size()
width = dim[0]
height = dim[1]
width += -1
x_init = random.randint(0,width-1)
y_init = random.randint(0,height-1)
x_speed = 1
y_speed = 1
fg_colors = ['red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white']
bext.fg(random.choice(fg_colors))
bext.goto(x_init,y_init) 
cbounce = 0

while True:
    x = x_init + x_speed
    y = y_init + y_speed
    if x == width-1 or x == 0:
        x_init = x
        y_init = y
        x_speed = x_speed*-1
        bext.fg(random.choice(fg_colors))
    if y == height-1 or y == 0:
        x_init = x
        y_init = y
        y_speed = y_speed*-1
        bext.fg(random.choice(fg_colors))
    if x == width-1 and y == 0:
        cbounce+=1
    if x == width-1 and y == height-1:
        cbounce+=1
    if x == 0 and y == height-1:
        cbounce+=1
    if x == 0 and y == 0:
        cbounce+=1
    print('>CORNER BOUNCES={}'.format(cbounce))    
    bext.goto(x,y) 
    print('DVD')
    x_init = x
    y_init = y
    time.sleep(0.05)
    clear()
