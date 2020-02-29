from sense_hat import SenseHat
import time
import sys

sense = SenseHat()

images = ["./luigi.png", "./mario.png", "./peach.png"]

def main():
    while True:
        for image in images:
            sense.load_image(image)
            time.sleep(2)

try:
    main()
except( SystemExit, KeyboardInterrupt ):
    pass
finally:
    print("done")