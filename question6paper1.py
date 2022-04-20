#trapisium methiod for integration
b = 10
a = 0
def f(x):
    return x**3 + x**2

def error(val):
    realval = 2833
    retVal = ((realval - val)/realval)*100
    if retVal < 0:
        return retVal * -1
    return retVal

def trapIntigrate(function,iterations, *args):
    sum = 0
    #sum func
    for xponent,weight in args:
        sum += weight*function(xponent)
    sum = (b-a)*sum
  
    print("error: {1},value: {2}".format(1, error(sum), sum))
    return sum



#a)

trapIntigrate(f,2,(a,0.5),(b,0.5))

#b)

trapIntigrate(f,3,(a,1/6),((a+b)/2,2/3),(b,1/6))

#c)
trapIntigrate(f,2,(-1.44337,0.5),(4.33,0.5))