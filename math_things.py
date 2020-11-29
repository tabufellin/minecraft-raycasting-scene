import struct
import numpy
from collections import namedtuple

V2 = namedtuple('Point2', ['x', 'y'])
V3 = namedtuple('Point3', ['x', 'y', 'z'])

def char(c):
	return struct.pack('=c', c.encode('ascii'))

def word(w):
	return struct.pack('=h', w)

def dword(d):
	return struct.pack('=l', d)

class color(object):
	def __init__(self, r, g, b):
		self.r = r
		self.g = g
		self.b = b

	def __add__(self, other_color):
		r = self.r + other_color.r
		g = self.g + other_color.g
		b = self.b + other_color.b

		return color(r, g, b)

	def __mul__(self, other):
		r = self.r * other
		g = self.g * other
		b = self.b * other
		return color(r, g, b)

	def __repr__(self):
		return "color(%s, %s, %s)" % (self.r, self.g, self.b)

	def toBytes(self):
		self.r = int(max(min(self.r, 255), 0))
		self.g = int(max(min(self.g, 255), 0))
		self.b = int(max(min(self.b, 255), 0))
		return bytes([self.b, self.g, self.r])

	def equals(self, other):
		return (self.r==other.r and self.g==other.g and self.b==other.b)

	__rmul__ = __mul__


def sum(v0, v1):
	return V3(v0.x + v1.x, v0.y + v1.y, v0.z + v1.z)

def sub(v0, v1):
	return V3(v0.x - v1.x, v0.y - v1.y, v0.z - v1.z)

def mul(v0, k):
	return V3(v0.x * k, v0.y * k, v0.z *k)

def dot(v0, v1):
	return v0.x * v1.x + v0.y * v1.y + v0.z * v1.z

def cross(v0, v1):
	return V3(
		v0.y * v1.z - v0.z * v1.y,
		v0.z * v1.x - v0.x * v1.z,
		v0.x * v1.y - v0.y * v1.x,
	)

def length(v0):
	return (v0.x**2 + v0.y**2 + v0.z**2)**0.5

def norm(v0):
	v0length = length(v0)

	if not v0length:
		return V3(0, 0, 0)

	return V3(v0.x/v0length, v0.y/v0length, v0.z/v0length)

def bbox(*vertices):
	xs = [ vertex.x for vertex in vertices]
	ys = [ vertex.y for vertex in vertices]

	xs.sort()
	ys.sort()

	xmin = xs[0]
	ymin = ys[0]
	xmax = xs[-1]
	ymax = ys[-1]

	return V2(xmin, ymin), V2(xmax, ymax)

def barycentric(A, B, C, P):
	bary = cross(
		V3(C.x - A.x, B.x - A.x, A.x - P.x),
		V3(C.y - A.y, B.y - A.y, A.y - P.y)
	)

	if abs(bary.z) < 1:
		return -1, -1, -1  

	u = cx/cz
	v = cy/cz
	w = 1 - (u + v)

	return V3(w, v, u)

def reflect(I, N):
	Lm = mul(I, -1)
	n = mul(N, 2 * dot(Lm, N))
	return norm(sub(Lm, n))

def refract(I, N, refractive_index):
	cosi = -max(-1, min(1, dot(I, N)))
	etai = 1
	etat = refractive_index

	if cosi < 0:
		cosi = -cosi
		etai, etat = etat, etai
		N = mul(N, -1)

	eta = etai/etat
	k = 1 - eta**2 * (1 - cosi**2)
	if k < 0:
		return V3(1, 0, 0)

	return norm(sum(
		mul(I, eta),
		mul(N, (eta * cosi - k**(1/2)))
	))

def finish(filename, width, height, pixels):
	f = open(filename, 'bw')

	# File header (14 bytes)
	f.write(char('B'))
	f.write(char('M'))
	f.write(dword(14 + 40 + width * height * 3))
	f.write(dword(0))
	f.write(dword(14 + 40))

	# Image header (40 bytes)
	f.write(dword(40))
	f.write(dword(width))
	f.write(dword(height))
	f.write(word(1))
	f.write(word(24))
	f.write(dword(0))
	f.write(dword(width * height * 3))
	f.write(dword(0))
	f.write(dword(0))
	f.write(dword(0))
	f.write(dword(0))

	for x in range(height):
		for y in range(width):
			f.write(pixels[x][y].toBytes())
	f.close()