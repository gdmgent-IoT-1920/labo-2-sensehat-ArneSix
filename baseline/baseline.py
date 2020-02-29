from sense_hat import SenseHat
import random
import time
import sys

sense = SenseHat()

def main():
    while True:
        ran_for_col = [ran(0,255), ran(0,255), ran(0,255)]
        ran_back_col = [ran(0,255), ran(0,255), ran(0,255)]

        sense.show_message("Hello! We are New Media Development :)", 0.1 ,ran_for_col, ran_back_col)

        time.sleep(2)

def ran(min, max):
    return random.randint(min, max + 1)

try:
    main()
except (KeyboardInterrupt ,SystemExit):
    print("program was interupted")
finally:
    sense.clear()
    sys.exit(0)