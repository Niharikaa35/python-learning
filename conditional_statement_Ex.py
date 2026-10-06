# if block



if True:
    print("This is IF Block")

print("IF is ended")


if False:
    print("This is IF Block")

print("IF is ended")

#write a programs whether  given number  is equal to 10
n=10
if n==10:
          print("It is 10")

          print("Ended")
#write a program which gives 15% discount if the price is grater then 5000 in bill

bp=5500
if bp>=5000:
    d=0.15
    total=bp-d
    print("bill befire discount",bp)
    print("after discount",total)
    
    # if else


    if False:
          print("True: If block executed")
    else:
          print("False:Else block is excuted")

    age=18
if age>=18:
      print("The age is above 18:",age)
else:
      print("Ended")

#write a program given number is equal to 10 or not
given_num=int(input("Enter the number"))
if given_num==10:
      print("The number is equal to  10")
else:
      print("the number is not equal to 10")


#write a program given number is + or -
num=int(input("Enter the number"))
if num>=0:
      print("Number is positive number")
else:
      print("Number is negative")

#write a program to check the biggest number among two values
first_num=int(input("Enter the a value"))
second_num=int(input("Enter the b value"))

if first_num>second_num:
      print("a   is greater then b ")
else:
      print("b is greater then a number")

#check given number is even or not
num_1=int(input("Enter number "))
num_2=int(input("Enter number"))
if num_1%2==0:
      print("This is even number")
else:
      print("this is not even number")

#check given number is not even
num_2=int(input("Enter number "))
if num_1%2!=0:
       print("This is not even number")

else:
      print("this is  even number")

#check given number is vowel or not
ch=str(input("Enter the alphabets"))
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
      print("Enterd alphabet is Vowel ")
else:
      print("not a vowel")

#write a program to check number given alphabet or not
ch=str(input("enter the value of ch"))
if ch>="A"and ch<="Z"or ch>="a"and ch<="z":
      print("ch is alphabet")
else:
      print("ch is not alphabet")
      
#write a program to check given value is digit or not
# digit=str(input("enter the value"))
# if digit>=0 and digit<=10:
#       print("entered value is digit")
# else:
#       print("not a digit")

    #write a program if name is hero and password is hero@123 login successfull otherwise it is invalid credentional 

name=str(input("Enter the name"))
pass_word =str(input("Enter the password"))
if name=="hero" and pass_word=="hero@123" or name=="Hero" or pass_word=="Hero@123":
      print("login successfull")
else:
      print("invalid credentional")
