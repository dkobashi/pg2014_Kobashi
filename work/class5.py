'''
Guide to use magic method in python
http://www.rafekettler.com/magicmethods.html
'''


class Point(object):
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def norm(self):
		import numpy as np
		return np.sqrt(self.x**2+self.y**2)

	def distance(self):
		return sqrt(self.x**2+self.y**2)

	def __add__(self,other):
		return Point(self.x+other.x, self.y,other.y)

	def __str__(self):
		return '(%f, %f)'%(self.x,self.y)

	def __repr__(self):
		return '(Print(%f,%f)'%(self.x,self.y)


if __name__ =='__main__':
	p1=Point(3.0,4.0)
	p2=Point(5.0,8.0)

	print p1, p2	
	p3=p1+p2
	print p3.x, p3.y



#example
import datetime
'''
class name often is capitalized distinguishing class from functions
'''
class UglyGPS(object):

	def __init__(self, filename):
		self.filename=filename
# 		self._filename=filename (adding _ make filename secret)

   		longitudes = []
    	latitudes = []
    	times = []

    	f=open(self.filename)
    
    	for line in f.readlines():
        	data = line.split(',')
        # $GPGGA,124628,4907.718,N,12312.802,W,2,06,1.30,5,M,,,,*29
        	if (data[0] == '$GPGGA') and (len(data) == 15):
            
           		hours = int(data[1][:2])
           		minutes = int(data[1][2:4])
            	seconds = int(data[1][4:])
            	time = datetime.time(hours, minutes, seconds)
            
            	lon = float(data[4])//100.0 + (float(data[4])%100.0)/60.0
            	lat = float(data[2])//100.0 + (float(data[2])%100.0)/60.0
            
            	times.append(time)
            	longitudes.append(lon)
            	latitudes.append(lat)

        self.time=times
        self.lat=latitudes
        self.lon=longitudes
    
  	    return times, longitudes, latitudes

if __name__ == '__main__':
    filename =  'ugly_gps_data1.dat'
    time, lon, lat = read_ugly_gps(filename)


#lecture (numpy)

import numpy as np
np.sqrt([1.0,2.0,3.0])
np.array([2.,3.,5.,10.])
np.array([1,2.,3.],'i')  #make data type integer (int32)
np.array([1,2,3,4],'f')  #make data type float (float32)

#make array
x=[]
for xx in range(10):
	x.append(xx)

from datetime import datetime
from datetime import timedelta

do=datetime(1970,1,1)
dt=timedelta(days=3)

dates=[do+n*dt for n in range(20)]  # this is for list
#or
dates=np.array([do+n*dt for n in range(20)]) # this is for array
# the results are same

month=[dates[n].month for n in range(20)]

python uses c-style memory allocation
[t,z,y,x] means x dimension has the fastest (right most dimension).
Fortran uess the opposite
[x,y,z,t] means x dimension has the fastest (left most dimension)


x.argmin()
x.argmax()

