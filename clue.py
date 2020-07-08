from __future__ import print_function

import mystery

import itertools
import time
import signal
import socket
import sys

UDP_IP = 'ft.noise'
UDP_PORT = 1337

screen0 = ("""
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X                                           X
X                                           X
X   XXXXXXXXXXX           XXXXXXXXXXXXX     X
X   XXXXXXXXXXXXXXXX      XXXXXXXXXXXXX     X
X   XXXXXXXXXXXXXXXXX     XXXXXXXXXXXXX     X
X   XXXXXX     XXXXXXX    XXXXX             X
X   XXXXXX      XXXXXXX   XXXXXXXXXXXX      X
X   XXXXXX       XXXXXX   XXXXXXXXXXXXXX    X
X   XXXXXX       XXXXXX   XXX    XXXXXXX    X
X   XXXXXX      XXXXXXX            XXXXXX   X
X   XXXXXX    XXXXXXXX   XX       XXXXXXX   X
X   XXXXXXXXXXXXXXXXX    XXXXXXXXXXXXXXX    X
X   XXXXXXXXXXXXXXX      XXXXXXXXXXXXXX     X
X   XXXXXXXXXXX             XXXXXXXX        X
X                                           X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
""") # 45x17

screen1 = ("""
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
X                                           X
X                                           X
X                                           X
X  XXXXXXXXXXXX   XXXXXXXXXX                X
X  XXXXXXXXXXXX   XXXXXXXXXX        XXX     X
X         XXXXX   XXXX            XXXXXXXX  X
X        XXXXX    XXXXXXXXX     XXXXXXXXXX  X
X       XXXXX     XXXXXXXXXXX  XXXX XXX     X
X      XXXXX            XXXXX  XXX  XXX     X
X     XXXXX      XX     XXXXX  XXXX XXX     X
X     XXXXX      XXXXXXXXXXX    XXXXXXXXXX  X
X    XXXXX        XXXXXXXXX       XXXXXXXX  X
X                                   XXX     X
X                                           X
X                                           X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
""") # 45x17


ntries = 30
success = False

for i in range(ntries):
    try:
        ft = mystery.Mystery(UDP_IP, UDP_PORT, 45, 35, layer=11)
        success = True
    except socket.gaierror:
        print("Connecting (%d/%d)" % (i + 1, ntries))
        time.sleep(5)
    if success:
        continue

if not success:
    print("Oh noes, there's a connection error!")
    print("Maybe the source will help you diagnose?")
    with open("clue.py", "r") as f:
        for line in f:
            print(line[:-1])
        sys.exit(0)

def signal_handler(signal, frame):
    print('Bye bye!')
    ft.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

for i in range(10):
    print("")

print("This screen is not big enough for this clue. Better look around for a better view :)")

for i in range(10):
    print("")

for screen in itertools.cycle((screen0, screen1)):
    for n in range(20):
        for y, line in enumerate(screen.split("\n")[1:]):
            for x, char in enumerate(line):
                b = (char == 'X') * 255
                b = b * ((x + y + n) % 9 != 0)
                ft.set(x, 2*y, (int(b*.9), int(b*.5), b))
                ft.set(x, 2*y + 1, (int(b*.5), int(b*.9), b))
        ft.send()
        time.sleep(.075)
    print("tic")
