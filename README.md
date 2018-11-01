# WS2812: Python class for the WS2812 NeoPixel display

This is a very short and simple class. It uses the RMT bus for driving WS2812
Neopixel  display.It is dedicated to Pycom devices

## Constructor

### ws2812 = WS2812(pin, channel=3)

- pin is the name of a GPIO pin, which can work as an output. The type of the
argument must be string.
- channel is the RMT channel to be used. Suitable values are 2 and 3.

## Method

### ws2812.show(pixels)

Display the color values define in pixels. pixels is a list to 3-Element tuples.
Each member of the list defines the colors of one WS2812 LED, the tuples define
the brightness of the green, red and blue led, each in the range of 0-255.
See also the example below.

## Interface

The WS2812 is connected to the RMT module. Only a single pin besides Vcc and GND is required.

The WS2812 need a Vcc of 5V. The data line of the WS2812 can be driven by the
output of the Pycom module, even at the limits of the spec. If the level is too
low, add a level converter with a bandwidth of >10 MHz between the GPIO pin of the
PyCom device and the WS2812 data input. You may also drive the WS2812 with a
somewhat lower voltage, like ~4V.

## Example

```
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

# define the colors for 24 Pixels
data = 6 * [
    (127, 0, 0),    # green
    (0, 127, 0),    # red
    (0, 0, 127),    # blue
    (127,127,127),  # white
    ]
# blank all 24 pixels
blank = 24 * [(0,0,0)]

ws2812 = ws2812.WS2812("P11")

while True:
    ws2812.show(data)
    sleep(1)
    ws2812.show(blank)
    sleep(1)```
