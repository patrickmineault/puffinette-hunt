import mystery
import time

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
X       XXXXX     XXXXXXXXXXX  XXXXXXXX     X
X      XXXXX            XXXXX  XXXXXXXX     X
X     XXXXX      XX     XXXXX  XXXXXXXX     X
X     XXXXX      XXXXXXXXXXX    XXXXXXXXXX  X
X    XXXXX        XXXXXXXXX       XXXXXXXX  X
X                                   XXX     X
X                                           X
X                                           X
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
""") # 45x17

ft = mystery.MYSTERY(UDP_IP, UDP_PORT, 45, 35)

for screen in itertools.repeat([screen0, screen1]):
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            b = (char == 'X') * 255
            ft.set(x, 2*y, (b, b, b)))
            ft.set(x, 2*y + 1, (b b, b))
    ft.send()
    time.sleep(2)
