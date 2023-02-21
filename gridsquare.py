'''
©2021 jon@gatorbot.com
Calcuate and convert gridsquares from latlngs.
'''
import argparse
import sys
from math import floor, trunc

class Gridsquare():
	"""
	Class Gridsquare

	Works with Maidenhead Grid Squares
	"""

	def __init__(self,lat=None, lng=None, clone=None): # default to home
		self.lat = 26.97611 if not lat else lat
		self.lng = -82.36151 if not lng else lng
		#deal with LatLng
		if (clone):
			self.lat, self.lng = clone.lat, clone.lng

		self.mls = ''
	
	@property
	def mls(self):
		return self._mls

	@mls.setter
	def mls(self, value=None):
		""" mls(): Returns Madenhead Locator System 8-digit grid square"""
		mls = ''
		X = self.lng + 180
		Y = self.lat + 90
		fields = "ABCDEFGHIJKLMNOPQR"
		sub_sqaures = 'abcdefghijklmnopqrstuvwx'

		#calculate field
		mls += fields[floor(X/20)]
		mls += fields[floor(Y/10)]
		#calculate square
		x = 10 * (X/20 - floor(X/20))
		y = 10 * (Y/10 - floor(Y/10))
		mls += str(floor(x))
		mls += str(floor(y))
		#calculate sub_square
		xx = x - floor(x)
		yy = y - floor(y)
		mls += sub_sqaures[floor(xx*24)]
		mls += sub_sqaures[floor(yy*24)]
		#calculate extended_square
		mls += str(floor((xx*24 - floor(xx*24))*10))
		mls += str(floor((yy*24 - floor(yy*24))*10))

		self._mls = mls


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--lat', help='decimal latidude (-90 – 90)', type=float)
	parser.add_argument('--lng', type=float, help='decimal longitude (-180 – 180)')
	args = parser.parse_args()

	g1 = Gridsquare(args.lat, args.lng)

	print('Maidenhead Locator System Gridsquare for {{latidude: {}, longitude: {}}} is: {}'.format(g1.lat, g1.lng, g1.mls))
