import pgzrun
import random

WIDTH = 600
HEIGHT = 600

def draw():
    screen.fill("black")
    s = 200
    for i in range (7):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        screen.draw.filled_circle((300,300),s,(r,g,b))
        s -= 25



pgzrun.go()