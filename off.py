#!/usr/bin/env python3

import sys
import blinkt

r=0
g=0
b=0

blinkt.set_clear_on_exit(True)
blinkt.set_all(r, g, b)
blinkt.show()
