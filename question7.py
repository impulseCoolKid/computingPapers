# goal find F_n
import matplotlib.pyplot as plt
import numpy as np

m = 1
k = 40
dt = 0.2
zeroNum = 20/dt
ycords = np.zeros(101)
xcoords = np.zeros(101)
yExact = np.zeros(101)

def xplusOne(f,t_stop,t_current = 0, x_0 = 0.01, x_1 = 0.01,pos=0):


    newX = f*dt**2/m - x_1 + 2*x_0 - dt**2*k*x_0/m
    ycords[pos]= newX
    xcoords[pos] = t_current
    t_current += dt
    print(t_current)
    if t_current >= t_stop:
        return newX
    else:
        newpos = pos + 1
        return xplusOne(f,t_stop,t_current,newX,x_0,newpos)

xplusOne(0,20)



#with force addded in the mix
def xplusOneFreal(t_stop,t_current = 0, x_0 = 0.01, x_1 = 0.01,pos=0):
    v = (x_0 - x_1)/dt
    def F(l):
        if l < 0.0:
             return 0.025
        elif l > 0.0:
            return -0.025
        else:
            return 0

    newX = F(v)*dt**2/m - x_1 + 2*x_0 - dt**2*k*x_0/m
    yExact[pos]= newX
    
    t_current += dt
    print(t_current)
    if t_current >= t_stop:
        return newX
    else:
        newpos = pos + 1
        return xplusOne(t_stop,t_current,newX,x_0,newpos)

xplusOneFreal


plt.plot(xcoords,yExact)
plt.plot(xcoords, ycords)
plt.show()