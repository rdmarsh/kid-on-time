#!/usr/bin/env python3

import sys
import blinkt

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


def stage(s):
    if s == '3':
	return [0,1,2,5,6,7]
    if s == '2':
	return [0,1,6,7]
    if s == '1':
	return [0,7]
    if s == '0':
	return []
    return [0,1,2,3,4,5,6,7]


def usage():
    print('Usage: {} <color> <stage>'.format(sys.argv[0]))
    sys.exit(1)


def main():
    if len(sys.argv) != 3:
   	usage()
    r,g,b = color(sys.argv[1])
    pixel = stage(sys.argv[2])
    blinkt.set_clear_on_exit(False)
    blinkt.clear()
    blinkt.show()
    for p in pixel:
	blinkt.set_pixel(p,r,g,b)
    blinkt.show()

if __name__ == '__main__':
    main()
