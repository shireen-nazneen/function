#if user enter the symbol we have to calculate#
def calculater(num,num2,oprator):
    if oprator=="+":
        return num+num2
    elif oprator=="//":
        return num//num2
    elif oprator=="/":
        return num/num2
    elif oprator=="+":
        return num+num2
    elif oprator=="**":
        return num**num2
    else:
        return num-num2
        
num=int(input("enter number"))
num2=int(input("enter number2"))
symbol=input("enter symbol")
print(calculater(num,num2,symbol))


# part(2)#
def calculater2(num1,num2,oprator):
    if oprator=="-":
       return num1-num2
    elif oprator=="+":
        return num1+num2
    else:
        return num1//num2
sum_nums=calculater2(2,6,"+")
print(sum_nums)
sum_nums2=calculater2(3,5,"-")
print(sum_nums2)
sum_nums3=calculater2(8,6,"//")
print(sum_nums3)

#part(3)#
def list_change(num1,num2,symbol):
    if symbol=="*":
        empty=[]
        i=0
        while i<len(num1):
            m=num1[i]*num2[i]
            empty.append(m)    
            i+=1
        return(empty)
multiple_list=list_change([1,2,4],[6,2,3],"*")
print(multiple_list)
    

