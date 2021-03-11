#grater number or eqaul number#
def check_numbers(num,num2):
    if num==num2:
        print("it is eqaul")
    elif num>num2:
        print("num is grater than num2")
    else:
        print("num2 is grater than")
check_numbers(19,1)
#wich number is gaarter in this list3
def check_numbers_list(num,num2):
    i=0
    while i<len(num):
        print(num[i]+num2[i])
        if num[i]>num2[i]:
            print(num[i],"grater than num2")
        elif num[i]==num2[i]:
            print(num[i],num2[i],"bot is eqal")
        else:
            print(num2[i],"num2[i] is grater")
        i+=1
check_numbers_list([2, 6, 18, 10, 3, 75] , [6, 19, 24, 12, 3, 87] )