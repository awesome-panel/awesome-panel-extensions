import math
def p_setup_gen(p):

  #--- p5 setup() function --------------------------
  def p_setup():
    p.createCanvas(200, 200)
    p.background(160)

  return p_setup

def p_draw_gen(p):

  #--- p5 draw() function ---------------------------
  def p_draw():
    p.fill('blue')
    fc = p.frameCount
    p.background(200)
    r = math.sin(fc/60) *50 + 50
    p.ellipse(100,100,r,r)

  return p_draw

def sketch_setup(p):
  p.setup = p_setup_gen(p)
  p.draw  = p_draw_gen(p)

myp5 = __new__ (p5(sketch_setup, 'sketch-holder'))