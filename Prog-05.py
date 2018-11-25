print("Report Card Generation")
#INCOMPLETE
user_marks=[]
user_subjects=[]
user_name= input("Enter your name: ")
user_id= int(input("Enter your unique id: "))

for sub in range(3):
    sub_name= input("Enter Subject" +str(sub+1) +":")
    sub_marks= int(input("Enter Subject" +str(sub+1) +" marks: "))
    user_marks.append(sub_marks)
    user_subjects.append(sub_name)
    if sub_marks > 100:
        print("Marks cannot be greater than 100")
        print("Please try again")
        break

print(u"\u25A0"*30)
print (": Subjects    : Score:")


for x in user_subjects:
    print(":",x[0:]," "*(10-len(x[0:])),":")
