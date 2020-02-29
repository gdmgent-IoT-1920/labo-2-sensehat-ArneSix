from sense_hat import SenseHat
import time
import sys

sense = SenseHat()

screen_w = 8
screen_h = 8

X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

fase1 = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, X, X, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]

fase2 = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, X, X, X, X, O, O,
    O, O, X, O, O, X, O, O,
    O, O, X, O, O, X, O, O,
    O, O, X, X, X, X, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]

fase3 = [
    O, O, O, O, O, O, O, O,
    O, X, X, X, X, X, X, O,
    O, X, O, O, O, O, X, O,
    O, X, O, O, O, O, X, O,
    O, X, O, O, O, O, X, O,
    O, X, O, O, O, O, X, O,
    O, X, X, X, X, X, X, O,
    O, O, O, O, O, O, O, O
]

fase4 = [
    X, X, X, X, X, X, X, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, O, O, O, O, O, O, X,
    X, X, X, X, X, X, X, X
]


loop_rect = [fase1, fase2, fase3, fase4]

def main():
    while True:

        for index, rect in enumerate(loop_rect, 0):
            sense.set_pixels(rect)
            time.sleep(0.1)
        
        for rect in reversed(loop_rect):
            sense.set_pixels(rect)
            time.sleep(0.1)


try:
    main()
except (SystemExit, KeyboardInterrupt):
    pass
finally:
    print("done")
    sense.clear()