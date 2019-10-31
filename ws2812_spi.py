from machine import SPI, disable_irq, enable_irq
from time import sleep, sleep_us


def send_spi(data, spi):
    no_pixel = len(data)
    buffer = bytearray(no_pixel * 3 * 4)
    index = 0
    for pixel in data:
        for byte in pixel:
            bits = 0
            mask = 0x80
            while mask:
                bits <<= 4
                if byte & mask:
                    bits |= 0x0e
                else:
                    bits |= 0x08
                mask >>= 1
            buffer[index] = (bits >> 24) & 0xff
            buffer[index + 1] = (bits >> 16) & 0xff
            buffer[index + 2] = (bits >> 8) & 0xff
            buffer[index + 3] = bits & 0xff
            index += 4
    sleep_us(60)  # ensure initial reset
    state = disable_irq()
    spi.write(buffer)
    enable_irq(state)

data = 6 * [
    (85, 0, 0),    # green
    (0, 85, 0),    # red
    (0, 0, 85),    # blue
    (85, 85, 85),   # white
    ]

blank = 24 * [(0, 0, 0)]
spi = SPI(SPI.MASTER, baudrate=3200000, polarity=0, firstbit=SPI.MSB, bits=32)

while True:
    send_spi(data, spi)
    sleep(1)
    send_spi(blank, spi)
    sleep(1)
