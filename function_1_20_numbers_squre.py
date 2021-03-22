# 1 to  20 each number of squre#
def dictionary(num):
    i=1
    dic={}
    while i<=num:
        dic[i]=i*i
        i=i+1
    return(dic)
a=dictionary(20)
print(a)