# question 1 a 
import math


n = 26*10**6

def liniarTime(m):
    return m*10**(-8)*n

def binAndqSort(m):
    return 2*10**(-5) * n * math.log(n) + m * 10**(-6)*math.log(n)

def compare(m):
    print("for m = {1}".format(1,m),"binary time",binAndqSort(m) ,"linear time",liniarTime(m),)
    if binAndqSort(m) > liniarTime(m):
        print("linear wins")
        return False
    print("binary and sort wins")
    return True
'''
#i
compare(10**3)
#ii
compare(10**4)
#iii
compare(3*10**5)
#iii
compare(5*10**5)  
'''

#question B
def contrast(m=34100):
    
    if compare(m):
        print("m")
        return m
    else:
        return contrast(m+1)

contrast()# value is 34150
