import * from pyp5js
import math

def p_setup():
    createCanvas(200, 200)
    background(160)

def p_draw():
    fill('blue')
    fc = p.frameCount
    background(200)
    r=math.sin(fc/60) *50 + 50
    ellipse(100,100,r,r)