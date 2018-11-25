def area_sq(lenght,breadth):
    area= lenght*breadth
    return area

sq_l= eval(input("Enter the lenght of square:    "))
sq_b= eval(input("Enter the breadth of square:   "))
sq_dec=int(input("Enter the decimals of output: "))
decimals= sq_dec
area= area_sq(sq_l, sq_dec)
print("The area of square with lenght " + str(sq_l) + " and breadth " +str(sq_b) + " is: {0:.{1}f}cm\u00b2".format(area, decimals)) 
