print("Projectile motion")
print(u"\u25A0"*17)

def f(Vx,t):
    x= Vx*t
    print("The horizontal distance at velocity: " +str(Vx)+ "m/s\nand time: " +str(t)+ "s\nis " +str(x)+"m")
def f2(Vx0):
    vx=Vx0
    print("The horizontal velocity is: " +str(vx)+"m/s")
def f3(Vy0,t):
    y=Vy0*t-1/2*9.81*t**2
    print("The verticle distance at initial velocity: "+str(Vy0)+"m/s\n and Time: " +str(t)+"s\n is: "+ str(y))
def f4(Vy0,t):
    vy=Vy0-9.8*t
    print("The verticle velocity at and initial velocity of: "+str(Vy0)+"m/s\nand Time: "+str(t)+"s\nis: " +str(vy)+"m/s")


Vx= eval(input("Please enter the velocity: "))
t= eval(input("Please enter the Time t:    "))
print(f(Vx,t))
Vx0=eval(input("Please enter initial velocity: "))
print(f2(Vx0))
Vy0=eval(input("Please enter the verticle distance: "))
t= eval(input("Enter time t:                        "))
print(f3(Vy0,t))
Vy0=eval(input("Please enter the initial velocity: "))
t= eval(input("Please enter time t:                "))
print(f4(Vy0,t))






    
    
    
