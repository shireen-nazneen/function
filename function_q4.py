#function sum of 2 numbers and sum of index of to list#
#part (1)
def add_num(num,num2):
    print(num+num2)
add_num(10,20)
#part(2)
def add_numbers_list(num1,num2):
    i=0
    while i<len(num1):
        print(num1[i]+num2[i])
        i+=1
add_numbers_list([4,4,3,55],[4,7,4,2])