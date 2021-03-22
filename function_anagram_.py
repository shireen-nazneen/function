def anagram(user1,user2):
    if len(user1)==len(user2):
        i=0
        c=0
        while i<len(user1):
            if user1[i] in user2:
                c+=1
            i+=1
        if c==len(user1):
            return(True)
        else:
            return(False)
    else:
        return(False)
var1=(input("enter words"))
var2=(input("enter words"))
a=anagram(var1,var2)
print(a)