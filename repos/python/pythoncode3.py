# TASK 3: Created a class with 5 instances
# Maneuvering the 5 aircrafts and then printing their coordinates.

class aircraft:
    x=3
    y=0
    acc=1

    def __init__(a, x, y):
        a.x = x
        a.y = y


a1=aircraft(4,0)
a2=aircraft(1,7)
a3=aircraft(0,2)
a4=aircraft(5,4)
a5=aircraft(8,1)



def moveup(y):
    y+=1
    return y

def moveleft(x):
    x-=1
    return x

def moveright(x):
    x+=1
    return x

def movedown(y):
    y-=1
    return y

y1=moveup(a1.y)
x1=moveright(a1.x)


print("\ncoordinates of airplane1:",x1,y1)

y2=movedown(a2.y)
x2=moveleft(a2.x)
print("\ncoordinates of airplane2:",x2,y2)

y3=moveup(a3.y)
x3=moveright(a3.x)
print("\ncoordinates of airplane3:",x3,y3)

y4=movedown(a4.y)
x4=moveleft(a4.x)
print("\ncoordinates of airplane4:",x4,y4)

y5=moveup(a5.y)
x5=moveright(a5.x)
print("\ncoordinates of airplane5:",x5,y5)
