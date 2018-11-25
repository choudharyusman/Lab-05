print("LAWS OF MOTION")
print(u"\u25A0"*14)
import math
def law_1(u,t):
    v= u+(9.81*t)
    print("The final velocity at an initial velocity of: "+str(u)+"m/s and Time "+str(t)+"s is: "+str(v)+"m/s")
def law_2(u,t):
    s=u*t+(1/2*9.81*t**2)
    print("The distance covered at an initial velocity of: "+str(u)+"m/s and Time "+str(t)+"s is: "+str(s)+"m")
def law_3(u,s):
    v= math.sqrt(u**2+2*(9.81*s))
    print("The final velocity at an initial velocity of: "+str(u)+"m/s and distance: "+str(s)+"m is: "+str(v))

user_inp= input("Please enter the desired law you wish to calculate: 1,2 or 3: ")
if user_inp=='1':
    u=eval(input("Please enter the initial velocity: "))
    t= eval(input("Please enter the time taken:      "))
    law_1(u,t)
if user_inp=='2':
    u=eval(input("Please enter the initial velocity: "))
    t= eval(input("Please enter the time taken:      "))
    law_2(u,t)
if user_inp=='3':
    u=eval(input("Please enter the initial velocity: "))
    s=eval(input("Please enter the distance covered: "))
    law_3(u,s)
else:
    print("Please Enter 1,2 or 3")
