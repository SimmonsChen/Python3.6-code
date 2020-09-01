import math

def square(x):
    return x*x
def distance(x1,y1,x2,y2):
    L=math.sqrt(square(x1-x2)+square(y1-y2))
    return L
def isTriangle(x1,y1,x2,y2,x3,y3):
    flag=((x1-x2)*(y3-y2)-(x3-x2)*(y1-y2))!=0
    return flag
