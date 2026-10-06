#1 find the profit percentage by using selling price and cost price 

# selling_price=int(input("Enter the selling Price"))
# cost_price=int(input("enter the cost price"))
# profit=selling_price-cost_price
# print("the profit is :",profit)
# profit_percentage=(profit/cost_price)*100
# print("the profit percentage is:",profit_percentage)

#2 find the missing angle in triangle by usimg 2 angles of triangle

# angle1=int(input("Enter the first angle"))
# angle2=int(input("enter the second angle"))
# angle3=(angle1+angle2)
# 180-angle3
# print(angle3)

#3 find the last digit of given number (% gives the reminder as output)

# number=int(input("Enter the  digits"))
# last_digit=(number)%10
# print(last_digit)

#4 Remove the last digit of given number ( // gives the quient as output)

# number=int(input("enter the number"))
# remove_digit=(number)//10
# print(remove_digit)

#5find the first digit of 4 digit number(/ by 1000)
# first_digit=int(input("enter the number of 4 digits "))
# four_digit=(first_digit)/1000
# print(four_digit)



# 6 find the sum of first natural number ((sum_natural=sum_natural+1)/2)
# n=int(input("enter the natural numbers"))
# sum_of=n(n)/2
# print("the sum is:",sum_of)

# 7 find the avg  of first natural number
# n=int(input("enter the value"))
# sum_of=n(n+1)/2
# sum_of=(sum_of)/2
# print("the avg is :",sum_of)


#8 find the gross salary basic sal is 20000 bonus=20%(0.2) incentive 5%(0.05)
salary=int(input("enter the salary"))
bonus=int(input("Enter bomus"))
incentives=int(input("Enter incentives"))
gross=salary+bonus+incentives
print("the gross salary is:",gross)

# 
basic_sal=2000
bonus_per=20
incentives_sal=5
bonus=bonus_per/100*basic_sal
incentives=incentives/100
print("bonus:",bonus)
print("incentives:",incentives)
gross=basic_sal+bonus+incentives
print("this is gross sal",gross)


#9 find inhand sal
basic_sal=2000
bonus_per=20
incentives_per=5
pf_per=2
hi_per=1

bonus=bonus_per/100*basic_sal
incentives=incentives/100
pf=pf_per/100*basic_sal
hi=hi_per/100*basic_sal
inhand_gross=basic_sal+bonus+incentives
deductables=pf+hi
inhand_gross=inhand_gross-deductables
print("this is in handd sal:",gross)

# 10 swap 2 numbers
#using three variables
a=10
b=20
c=a
a=b
b=c
print(a,b)

#using two variables
a=int(input("Enter the value"))
b=int(input("enter the value"))
a= a+b 
b= a-b 
a= b-a
print(a, b)


#TRUTHY AND FALSY

if(""):
    print("if condition is true if block excutes")
else:
    print("if condition is false else block excutes")


if(-1):
    print("if condition is true if block excutes")
else:
    print("if condition is false else block excutes")







