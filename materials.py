from color import color

class Material(object):
  def __init__(self, diffuse=color(0,0,0), albedo=(1, 0), spec=0, refractive=0):
    self.diffuse = diffuse
    self.albedo = albedo
    self.spec = spec
    self.refractive = refractive


red_bowl = Material(diffuse=color(180, 0, 0), albedo=(0.6,  0.3, 0.1, 0), spec=10)
white_skin = Material(diffuse=color(255, 255, 255), albedo=(1,  1, 1, 0), spec=40)
brown_skin = Material(diffuse=color(255, 204, 153), albedo=(0.2,  0.3, 1, 0), spec=20)
eye = Material(diffuse=color(50, 50, 50), albedo=(0.2,  0.3, 1, 0), spec=10)
brown_skin_extra = Material(diffuse=color(150, 60, 50), albedo=(0.2,  0.3, 0.2, 0), spec=10)
gold =Material(diffuse=color(255, 241, 33), albedo=(0.6, 0.3, 0.1, 0), spec=50, refractive=0)
water = Material(diffuse=color(51, 83, 152), albedo=(0.3, 0.3, 0.3, 0), spec=50, refractive=2)
stone = Material(diffuse=color(77, 77, 77), albedo=(0.3, 0.3, 0.3, 0), spec=20, refractive=0)
land = Material(diffuse=color(48, 44, 28), albedo=(0.3, 0.3, 0.3, 0), spec=60, refractive=0)
grass = Material(diffuse=color(204, 255, 204), albedo=(0.3, 0.3, 0.3, 0), spec=60, refractive=0)
