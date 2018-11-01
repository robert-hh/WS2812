#
# sample code for the WS2812 class
#
# Connections:
# xxPy | WS2812
# -----|-------
# Vin  |  Vcc
# GND  |  GND
# P11  |  DATA
#
import ws2812
from utime import sleep

data = 6 * [
    (127, 0, 0),    # green
    (0, 127, 0),    # red
    (0, 0, 127),    # blue
    (127,127,127),  # white
    ]

blank = 24 * [(0,0,0)]

ws2812 = ws2812.WS2812("P11")

while True:
    ws2812.show(data)
    sleep(1)
    ws2812.show(blank)
    sleep(1)
