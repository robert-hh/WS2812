#
# class for driving WS2812 Neopixel device on a Pycom 
# module using the RMT interface
#

class WS2812:
    def __init__(self, pin, channel=3):
        from machine import RMT
        self.rmt = RMT(channel=channel, gpio=pin, tx_idle_level=0)
        
    def show(self, data):
        from time import sleep_us
        no_pixel = len(data)
        bits = bytearray(no_pixel * 24 * 2)
        duration =  bytearray(no_pixel * 24 * 2)
        index = 0
        for pixel in data:
            for byte in pixel:
                mask = 0x80
                while mask:
                    bits[index] = 1
                    bits[index+1] = 0
                    if byte & mask:
                        duration[index] = 8
                        duration[index+1] = 4
                    else:
                        duration[index] = 4
                        duration[index+1] = 8
                    index += 2
                    mask >>= 1
        sleep_us(60) # wait for the reset time
        self.rmt.pulses_send(tuple(duration), tuple(bits))
        sleep_us(60) # wait for the reset time

