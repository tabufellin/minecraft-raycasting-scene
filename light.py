from math_things import V3

class Light(object):
	def __init__(self, position=V3(0,0,0), intensity=0):
		self.position = position
		self.intensity = intensity
		