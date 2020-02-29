from sense_hat import SenseHat
import sys
import time
import random
import os

sense = SenseHat()
sense.set_imu_config(False, False, False)
sense.set_rotation(90)

input_str = str(input("Enter the text to display: "))
letter_delay = float(input("Enter the delay between letter's shown: "))
loop_delay = float(input("Enter the loop delay: "))

list_str = [char for char in input_str]

def main():
    while True:

        for char in list_str:
            rr = random.randint(0,256)
            rg = random.randint(0,256)
            rb = random.randint(0,256)

            sense.show_letter(char, [rr, rg, rb])
            time.sleep(letter_delay)
        
        sense.clear()


        time.sleep(loop_delay)

try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("closed")
finally:
    sense.clear()
    sys.exit(0)