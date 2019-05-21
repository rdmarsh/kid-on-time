#!/usr/bin/python3

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

