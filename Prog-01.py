import math
def area_cyl(height,radius):
    area= (2*math.pi*radius*height)+(2*math.pi*radius**2)
    return area
def volume_cyl(height,radius):
    volume= math.pi*radius**2*height
    return volume

cyl_h=eval(input("Please enter the cylinder's height:          "))
cyl_r=eval(input("Please enter the cylinder's radius:          "))
dec_a= int(input("Enter the number of decimals of your output: "))
area= area_cyl(cyl_h,cyl_r)
volume= volume_cyl(cyl_h,cyl_r)
decimals=dec_a
print("The area of the cylinder is {0:.{1}f}cm\u00b2".format(area, decimals))
decimals=dec_a
print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume, decimals))
