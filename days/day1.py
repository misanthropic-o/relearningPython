 #name = input("enter you name")

#print(name)

#x = int(input("enter number x"))
#y = int(input("enter number y"))

#sum = x + y
#print(sum)

#num = int(input("enter a number"))

#def even_or_odd(num):
   # if (num%2) == 0:
    #    print("the number is even")
   # else:
       #print("the numberi s odd")

# result = even_or_odd(num)

# stringUsr = input("enter a string")

# print(len(stringUsr))

usrChoice = int(input("write 1 for , 2 for cel to fah"))
temp = int(input("write the temperature"))

def tempConv(usrChoice, temp):
    if usrChoice == 1:
        celToFah = (((9/5)*(temp))+32)
        print(celToFah)
    elif usrChoice == 2:
        fahToCel = ((5/9)*(temp-32))
        print(fahToCel)

tempConv(usrChoice, temp)