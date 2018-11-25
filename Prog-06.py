print("NEWTON'S LAWS OF MOTION")
print(u"\u25A0"*23)

def law_1():
    print("Newton's 1st law of motion\n",u"\u25A0"*25)
    print("It states only that a body at rest will remain at rest unless an outside force acts on it, and a body in motion at a constant velocity will remain in motion in a straight line unless acted upon by an outside force. ")
def law_2(m,a):
    print("Newton's 2nd law of motion\n", u"\u25A0"*25)
    print("The second law states that the acceleration of an object is dependent upon two variables - the net force acting upon the object and the mass of the object.")
    F= m * a
    return F
def law_3():
    print("Newton's 3rd law of motion\n", u"\u25A0"*25)
    print("The Third Law of Motion states:\nFor every action, there is an equal and opposite reaction.")
print(law_1())
m=eval(input("Enter mass of object: "))
a=eval(input("Enter acceleration of object: "))
print(law_2(m,a))
print(law_3())
