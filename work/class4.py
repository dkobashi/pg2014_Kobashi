
hour=100
minute=200
print '%6.3f %4.2f' % (hour, minute)

from datetime import datetime, timedelta

now=datetime.now()
print now

dt=timedelta(hours=3)
print dt

newtime=now+dt
print newtime

print newtime-now


class Point(object):
	'''doc string for point'''
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def norm(self):
		import numpy as np
		return np.sqrt(self.x**2+self.y**2)

	def __add__(self,other):
		return Point(self.x+other.x, self.y,other.y)
		
