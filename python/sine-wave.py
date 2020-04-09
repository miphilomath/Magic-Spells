import math
import time

numCycle = 5
step = 0.3
amp = 20
axis_shift = 21
pi = math.pi
pointer = '.'

def sin(x):
    return math.sin(x)

x = 0
while x < (2 * pi * numCycle):
    bar = int(amp * sin(x))
    x += step
    print((axis_shift + bar) * pointer)
    time.sleep(0.03)

