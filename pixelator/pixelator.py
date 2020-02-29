from sense_hat import SenseHat
import time
import sys
import random

ROWS = 8
COLUMNS = 8

sense = SenseHat()

sense.set_rotation(270)


def main():
    while True:
        for row in range(ROWS):
            for col in range(COLUMNS):
                sense.set_pixel(row, col, r_color())
                time.sleep(0.5)
        
        sense.clear()

def r_color():
    return (random.randint(0,256), random.randint(0,256), random.randint(0,256))

try:
    main()
except (KeyboardInterrupt, SystemExit):
    pass
finally:
    print("done")
    sense.clear()
    sys.exit(0)