#double intigral integration func
import math

def function1(x,y):
    e = 2.718281828
    return e**(x*y) * math.cos(x)**2 * math.sin(y**2)
    #e**(aArray[integer]*bArray[integer]) * math.cos(aArray[integer])**2 * math.sin(bArray[integer]**2)


def moteCarloInt(N,a,b,func):
    aArray =[]
    bArray = []
    def arraygGen(arr, value):
       
        avVal =value/(N/2)

        for numbers in range(N):
            arr.append(numbers*avVal - value)
        
    arraygGen(aArray, a)
    arraygGen(bArray,b)

    e = 2.718281828
    sum = 0
    for integer in range(N):
        sum += func(aArray[integer,bArray[integer]])

    f = 1/N * sum
    return f 

    
    
print(moteCarloInt(10**2,1,1,function1))

# for predicting pi

def piFunc(x,y):

    #not entirely sure about the pi func


        
