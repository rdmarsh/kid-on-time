#!/usr/bin/env python3

import sys
import math
import time
import blinkt

num=math.trunc(time.time()/86400)


def color(c):
    if c == 'red':
        return 255,0,0
    if c == 'green':
        return 0,255,0
    if c == 'blue':
        return 0,0,255
    if c == 'yellow':
        return 255,255,0
    if c == 'orange':
        return 255,64,0
    if c == 'magenta':
        return 255,0,255
    if c == 'cyan':
        return 255,255,0
    if c == 'white':
        return 255,255,255
    if c == 'off':
        return 0,0,0
    return 0,0,0


alt='off'
s=1
if num % 2 == 0:
    #josh blue even 
    c = 'blue'
else:
    #simon red odd
    c = 'red'

blinkt.set_clear_on_exit(False)

#turn off for 1 second
r,g,b = color(alt)
blinkt.set_all(r,g,b)
blinkt.show()
time.sleep(s)

#then turn on
r,g,b = color(c)
blinkt.set_all(r,g,b)
blinkt.show()
