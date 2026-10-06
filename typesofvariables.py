
# static variable
class VariableEX:
    name="niharika" #static variable

    @staticmethod
    def m1():
        print("I am static variable",VariableEX.name)

@staticmethod
def m2():
        print("accessing m1 method variable",VariableEX.name)

        VariableEX.m1()
        VariableEX.m2()


class test:
     def m1(self):
          self.name="hello"
          print("this is instance method",self.name) 

t=test()
t.m1()

# Instance Variable
class test1:
     def m1(self):
          self.name="hero"
          print("this is m1",self.name)
     def m2(self):
          print("this is m2",self.name)

t=test1()
t.m1()
t.m2()
          

# creating instance variables by using obj

class displaytest:
     def display(self):
          print("Name is ",self.name,"Age is", self.age,"Gender is",self.g)
t=displaytest()
t.name="Niharika"
t.age=25
t.g="F"

t.display()


# class student:
#      def studetails(self):
#           print("name is ",self.name)
#           print("age is ",self.age)
#           print("course is ",self.course)

# std1=student
# std1.name="niharika"
# std1.age=25
# std1.course="python"
# std1.studetails()
          
# std2=student
# std2.name="niha"
# std2.age=25
# std2.course="java"
# std2.studetails()       


class Student:
     def assigndata(self,name,age,course):
        self.myname=name
        self.myage=age
        self.mycourse=course
        
     def studetailss(self):
          print("name is ",self.myname)
          print("age is ",self.myage)
          print("course is ",self.mycourse)

s1=Student()
s1.assigndata("niharika",22,"python")
s1.studetailss()

s2=Student()
s2.assigndata("niha",22,"java")
s2.studetailss()

s3=Student()
s3.assigndata("harika",22,"dot net")
s3.studetailss()



class emp:
     ofcname="Innomatics"  #static variable
     def assigndata(self,name,age):
          self.myname=name
          self.myage=age
     def empdetails(self):
          print("the name of emp is",self.myname)
          print("the age of emp is",self.myage)
          print("the office name of emp is",emp.ofcname)

s1=emp()
s1.assigndata("niharika",22)
s1.empdetails()
