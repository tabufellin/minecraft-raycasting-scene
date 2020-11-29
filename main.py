
from raytracer import Raytracer
from sphere import *
from materials import *
from math_things import V3
from light import Light
from cube import *
from plane import *
r = Raytracer(100, 100)

r.light = Light(
  position=V3(30, 20, 20),
  intensity=1.8
)

r.background_color = color(161,245,247)

r.scene = [
  #Sphere(V3(-5, 0, -10), 3, brown_skin),
  Cube(V3(-5, -3, -10),3, water),
  Cube(V3(-5, 3, -13),3, water),
  Cube(V3(-5, 0, -10),3, water),
  Cube(V3(-5, 0, -13),3, water),
  Cube(V3(-5, 3, -13),3, water),

  Cube(V3(0, -3, -10),3, gold),
  Cube(V3(0, 0, -13),3, gold),
  Cube(V3(0, 3, -16),3, gold), 

  Cube(V3(5, -3, -10),3, water),
  Cube(V3(5, -3, -13),3, water),
  Cube(V3(5, 0, -10),3, water),
  Cube(V3(5, 0, -13),3, water),
  Cube(V3(5, 3, -13),3, water), 

  Cube(V3(0, -6, -10),3, stone),
  Cube(V3(3, -6, -10),3, stone), 
  Cube(V3(6, -6, -10),3, stone), 
  Cube(V3(-3, -6, -10),3, stone),
  Cube(V3(-6, -6, -10),3, stone),  
  
  Cube(V3(0, -6, -13),3, stone),
  Cube(V3(3, -6, -13),3, stone), 
  Cube(V3(6, -6, -13),3, stone), 
  Cube(V3(-3, -6, -13),3, stone),
  Cube(V3(-6, -6, -13),3, stone),

  Cube(V3(0, -6, -16),3, stone),
  Cube(V3(3, -6, -16),3, stone), 
  Cube(V3(6, -6, -16),3, stone), 
  Cube(V3(-3, -6, -16),3, stone),
  Cube(V3(-6, -6, -16),3, stone),

  Cube(V3(0, -3, -19),3, stone),
  Cube(V3(3, -3, -19),3, stone), 
  Cube(V3(6, -3, -19),3, stone), 
  Cube(V3(-3, -3, -19),3, stone),
  Cube(V3(-6, -3, -19),3, stone),

  Cube(V3(0, 0, -19),3, stone),
  Cube(V3(3, 0, -19),3, stone), 
  Cube(V3(6, 0, -19),3, stone), 
  Cube(V3(-3, 0, -19),3, stone),
  Cube(V3(-6, 0, -19),3, stone),

  Cube(V3(0, 3, -19),3, land),
  Cube(V3(3, 3, -19),3, land), 
  Cube(V3(6, 3, -19),3, land), 
  Cube(V3(-3, 3, -19),3, land),
  Cube(V3(-6, 3, -19),3, land),

  Cube(V3(0, 5, -19),2, grass),
  Cube(V3(2, 5, -19),2, grass), 
  Cube(V3(4, 5, -19),2, grass), 
  Cube(V3(-2, 5, -19),2, grass),
  Cube(V3(-4, 5, -19),2, grass),
  
  #Sphere(V3(4.6, -1.3, -15), 2, red_bowl),

  #Sphere(V3(2.9, 0, -14.5), 1.1, brown_skin),

  
]
r.envmap = None
r.render()
r.write('out.bmp')