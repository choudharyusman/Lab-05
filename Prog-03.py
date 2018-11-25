def arith_seq(f_term,com_diff):
    user_dec= input("Do you want to continue or not?: ")
    while user_dec== 'yes' :
        n_term= eval(input("Please enter the nth term you wish to calculate: "))
        an=f_term+(n_term-1)*com_diff
        return an

f_term= eval(input("Please enter the first term: "))
com_diff= eval(input("Please enter the second term: "))
print(arith_seq(f_term,com_diff))
