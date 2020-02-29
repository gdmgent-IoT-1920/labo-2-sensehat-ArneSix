from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import time
import sys

sense = SenseHat()
sense.set_rotation(90)

x = 4
y = 4

snake_segements = [[4, 4], [4, 5]]

def main():
    sense.stick.direction_down = pushed_down
    sense.stick.direction_left = pushed_left
    sense.stick.direction_right = pushed_right
    sense.stick.direction_up = pushed_up
    sense.stick.direction_any = refresh

    refresh()
    pause()

def pushed_up(event):
    if event.action != ACTION_RELEASED:
        move_up()

def pushed_down(event):
    if event.action != ACTION_RELEASED:
        move_down()

def pushed_left(event):
    if event.action != ACTION_RELEASED:
        move_left()

def pushed_right(event):
    if event.action != ACTION_RELEASED:
        move_right()

def refresh():
    sense.clear()
    check_bounds()
    draw_mario()

def draw_mario():
    print(snake_segements)
    for index, coord in enumerate(snake_segements, start=0):
        if index == 0:
            sense.set_pixel(coord[0], coord[1], 39, 24, 242)
        else:
            sense.set_pixel(coord[0], coord[1], 0, 255, 0)

def clamp(value, min_value = 0, max_value = 7):
    return min(max_value, max(min_value, value))

def move_up():
    snake_segements.append([x,y])

    snake_segements[0][1] += 1

def move_down():
    snake_segements[0][1] -= 1

def move_right():
    snake_segements[0][0] += 1

def move_left():
    snake_segements[0][0] -= 1

def check_bounds():
    if (snake_segements[0][0] < 0 or
        snake_segements[0][0] > 7 or
        snake_segements[0][1] < 0 or
        snake_segements[0][1] > 7):
        sense.show_message("GAME OVER")


try:
    main()
except (KeyboardInterrupt, SystemExit):
    print("Program was interupted")
finally:
    sense.clear()
    sys.exit(0)