#HW1.1
##Fibonacci Numbers
def fib(n=100):
    import numpy as np
    import matplotlib.pyplot as plt
    f=np.zeros((n))

    f[0]=0.0
    f[1]=1.0
    f[2]=1.0
    for i in np.arange(2,len(f),1):
        f[i]=f[i-1]+f[i-2]
        print f
    
    x=range(n)
    plt.plot(x,f)
    plt.show()
    
    return f

fib(5)
##

##function to compute integral using trapezoidal rule
def integrate(f,dx=1.0):
    import numpy as np
    n=len(f)
    integral=np.zeros((n-1))
    for i in range(n-1):
        integral[i]=dx*(f[i]+f[i+1])/2.0
    
    print np.sum(integral)
    
    return integral

integrate(range(5),dx=.5)
##

##function to read discharge.dat, return a list of dates as datetime objects and discharge
def discharge(fname):
    from dateutil import parser 
    
    f=open(fname)
    lines=f.readlines()
    date_time=[]
    discharge=[]
    n=-1
    for line in lines:
        lsplit=line.split()
        if lsplit[0][0]=='#':
            pass
        else:      
            n+=1
            if n==0:
                dtime=parser.parse(lsplit[2])
                date_time.append(dtime)
                discharge.append(float(lsplit[3][:-2]))
            else:
                dtime=parser.parse(lsplit[2])
                date_time.append(dtime)
                try:
                    discharge.append(float(lsplit[3][:-2]))
                except:
                    discharge.append(float(lsplit[3][:-4]))
                    
    make_plot=True
    if make_plot:      
        import matplotlib.pyplot as plt
        plt.plot_date(date_time,discharge,'k-')
        plt.show()
    
    return date_time, discharge
    
discharge('discharge.dat')
##

                                        
##function to read drifter.dat, return a list of data
def drifter(fname):
    
    import numpy as np
    
    f=open(fname)
    lines=f.readlines()
    longitude=[]
    latitude=[]
    tracks={}
    x=[]
    name=[]
    for line in lines:
        lsplit=line.split('\t')
        if lsplit[0]=='Track':
            name=lsplit[1]
        if lsplit[0]=='Trackpoint':
            llsplit=lsplit[1].split()

            latitude=llsplit[1]
            longitude=llsplit[3]
            x.append([name,longitude,latitude])
    
    def get_list(x):
        nx=len(x)
        sta_list=[x[i][0] for i in range(nx)]
        sta_name=set(sta_list)
        
        return sta_name
        
    nx=len(x)
    y=[]
    for sta in sta_name:
        for ix in range(nx):
            if x[ix][0]==sta:
                y=np.vstack((x[ix][1],x[ix][2]))
        tracks[sta] = y 
    
    return tracks

drifter('drifter.dat')

##