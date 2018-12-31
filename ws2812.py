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
        duration = bytearray(len(data) * 24 * 2)
        index = 0
        for pixel in data:
            for byte in pixel:
                mask = 0x80
                while mask:
                    duration[index:index+2] = \
                        b'\x08\x04' if byte & mask else b'\x04\x08'
                    index += 2
                    mask >>= 1
        sleep_us(60)  # wait for the reset time
        self.rmt.pulses_send(tuple(duration), (1, 0) * (len(data) * 24))
