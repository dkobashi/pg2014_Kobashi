

#function

def add_five(x,y,z):
    """
    Return input values plus five
    """
    b=x+y+z+5.0
    return b
#    pass

print add_five(1.,2.,3.)



#find line with GPGLL
def read_ugly_gps(filename):
	from datetime import datetime
#	filename='ugly_gps_data1.dat'

	f=open(filename)
	for line in f.readlines():
    	data = line.split(',')
#    if data[0] == '$GPGLL':
#       print line,
    	if (data[0]=='$GPGGA') and (len(data) ==15):
  		  	hour=int(data[1][:2])
   	 		minute=int(data[1][2:4])
    		second=int(data[1][4:])
   		 	print '%d:%d:%d Z' % (hour,minut,second)
    		time = datetime.time(hour,minute,second)
    		print time

if __name__ =='__main__':
	filename='ugly_gps_data1.dat'
	time,lon,lat=read_ugly_gps(filename)